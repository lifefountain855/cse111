jscodesnip = """
import{world,system,CommandPermissionLevel,CustomCommandParamType,CustomCommandStatus}from"@minecraft/server";import{songs}from"./songs.js";function log(s){world.sendMessage(`${s}`)}let stopsong=0;system.beforeEvents.startup.subscribe((({customCommandRegistry:s})=>{s.registerCommand({name:"wsp:start",description:"Start a song.",permissionLevel:CommandPermissionLevel.Any,cheatsRequired:!1,mandatoryParameters:[{name:"song",type:CustomCommandParamType.String}]},((s,e)=>{if(!s.sourceEntity)return{status:CustomCommandStatus.Failure};if(songs[e]){const s=world.getDimension("overworld");system.runTimeout((()=>{world.sendMessage(`§7Starting song: §l§a${e}§r§7...§r`)}),5);const t=system.currentTick,n=system.runInterval((()=>{let o=system.currentTick-t,r=songs[e].filter((s=>20*s.absolute_seconds==o&&"note_on"==s.message));if(0!=r.length)for(let e=0;e<r.length;e++){let t=r[e];world.sendMessage(`§7Note: §l§a${t.note_name}§r §7@pitch: §l§a${t.minecraft_pitch}§r\n§7 @tick: §l§a${o}§r\n§7 @instrument: §l§a${t.instrument}§r`),s.runCommand(`execute at @a run playsound note.${t.instrument} @a ~ ~ ~ 1 ${t.minecraft_pitch}`)}1==stopsong&&(world.sendMessage(`§7Song stopped: §l§a${e}§r`),system.clearRun(n),stopsong=0)}),0);system.runTimeout((()=>{system.clearRun(n),world.sendMessage(`§7Song finished: §l§a${e}§r`)}),20*songs[e].at(-1).absolute_seconds+2)}else world.sendMessage(`§l§4Error:§r §4Song not found: ${e}§r`)})),s.registerCommand({name:"wsp:stop",description:"Stop the current song.",permissionLevel:CommandPermissionLevel.Any,cheatsRequired:!1},((s,e)=>{if(!s.sourceEntity)return{status:CustomCommandStatus.Failure};stopsong=1}))}));"""
songsjs="""
// this is scripts/songs.js
export const songs={
    "[SONG]":[PUT_DATA_HERE]
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

