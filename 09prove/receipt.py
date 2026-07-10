import csv
from datetime import datetime, date
import qrcode

STORE_NAME="Inkom Emporium"

def fetch_products(filename):
    product_dict={}
    try:
        with open(filename, "rt") as csvfile:
            reader= csv.reader(csvfile, strict=True)
            next(reader)
            i=0
            for row in reader:
                # print(row)
                product_dict[row[0]]={"productName":row[1],"price":row[2]}
                i+=1
    except FileNotFoundError as err: 
        print("Error: file not found")
    return product_dict

def process_request(file,dict):
    try:
        with open(file, "rt") as csvfile:
            print(STORE_NAME,"\n")
            subtotal=0
            items=0
            reader= csv.reader(csvfile, strict=True)
            next(reader)
            for row in reader:
                try:
                    item=dict[row[0]]
                except KeyError: print(f"Error: unknown product ID in the request.csv file {row[0]}"); return
                subtotal+=float(item["price"])*float(row[1])
                items+=int(row[1])
                print(f"{item["productName"]}: {row[1]} @ {item["price"]}")
        now=datetime.now()
        storeurl=f"https://{STORE_NAME.lower().strip().replace(" ","_")}.com/survey"
        print(f"""\nNumber of Items: {items}
Subtotal: {round(subtotal,2)}
Sales Tax: {round(subtotal*0.06,2)}
Total: {round(subtotal*1.06,2)}

Thank you for shopping at the {STORE_NAME}.
{now.strftime("%B %d  %H:%M:%S  %Y")}
Make sure to fill out our survey at {storeurl}""")
        qr = qrcode.QRCode()
        qr.add_data(storeurl)
        qr.print_ascii()
    except FileNotFoundError as err: 
        print("Error: file not found")
    return

def main():
    products_dict=fetch_products("09prove/products.csv")
    process_request("09prove/request.csv",products_dict)
    return

if __name__ == "__main__":
    main()