jscodesnip = """
// this is scripts/index.js
import { world, system, CommandPermissionLevel, CustomCommandParamType, CustomCommandStatus, } from '@minecraft/server';
import { songs } from './songs.js'

function log(l){
    world.sendMessage(`${l}`)
}

let stopsong=0;
system.beforeEvents.startup.subscribe(({ customCommandRegistry }) => {
    customCommandRegistry.registerCommand(
        {
            name: "wsp:start",
            description: "Start a song.",
            permissionLevel: CommandPermissionLevel.Any,
            cheatsRequired: false,
            mandatoryParameters: [
                { name: "song", type: CustomCommandParamType.String },
            ],
        },
        (origin, song) => {
            // Only run if executed by an entity
            if (!origin.sourceEntity)
                return {
            status: CustomCommandStatus.Failure,
        };
        
        if (songs[song]) {
            const ovw=world.getDimension("overworld")
            system.runTimeout(()=>{
                world.sendMessage(`§7Starting song: §l§a${song}§r§7...§r`)
            }, 5)
            const inittick=system.currentTick;
            const callbacksong = system.runInterval(()=>{
                let songtick=system.currentTick-inittick
                // log(songtick)
                let matches = songs[song].filter((msg)=>((msg["absolute_seconds"]*20==songtick)&&(msg["message"]=="note_on")))
                if (matches.length!=0){
                    for (let i=0;i<matches.length;i++){
                        let match=matches[i]
                        world.sendMessage(`§7Note: §l§a${match["note_name"]}§r §7@pitch: §l§a${match["minecraft_pitch"]}§r\n§7 @tick: §l§a${songtick}§r\n§7 @instrument: §l§a${match["instrument"]}§r`)
                        ovw.runCommand(`execute at @a run playsound note.${match["instrument"]} @a ~ ~ ~ 1 ${match["minecraft_pitch"]}`)
                    }
                }
                if (stopsong==1){
                    world.sendMessage(`§7Song stopped: §l§a${song}§r`)
                    system.clearRun(callbacksong)
                    stopsong=0;
                }
            },0)
            system.runTimeout(()=>{
                system.clearRun(callbacksong)
                world.sendMessage(`§7Song finished: §l§a${song}§r`)
            }, (songs[song].at(-1)["absolute_seconds"]*20)+2)
        } else {
            world.sendMessage(`§l§4Error:§r §4Song not found: ${song}§r`)
        }

        }
    );

    customCommandRegistry.registerCommand(
        {
            name: "wsp:stop",
            description: "Stop the current song.",
            permissionLevel: CommandPermissionLevel.Any,
            cheatsRequired: false,
        },
        (origin, song) => {
            // Only run if executed by an entity
            if (!origin.sourceEntity)
                return {status: CustomCommandStatus.Failure,};
            stopsong=1;
        }
    );
});"""
songsjs="""
// this is scripts/songs.js
export const songs={
    "[SONG]":[[$$$]]
}
"""

manifest="""
{
	"format_version": 2,
	"header": {
		"name": "§l§aNotes§r",
		"description": "[ENTER DESCRIPTION]",
		"uuid": "[ENTER UUID]",
		"version": "1.0.0",
		"min_engine_version": [
			1,
			21,
			114
		]
	},
	"modules": [
		{
			"uuid": "[ENTER UUID]",
			"version": "1.0.0",
			"type": "script",
			"language": "javascript",
			"entry": "scripts/index.js"
		},
		{
			"type": "data",
			"uuid": "[ENTER UUID]",
			"version": "1.0.0"
		}
	],
	"dependencies": [
		{
			"module_name": "@minecraft/server",
			"version": "2.8.0"
		}
	]
}"""

