import url_data
def qrdata(barcodeData,barcodeType):
    string = "Data: " + str(barcodeData) + " | Type: " + str(barcodeType)
    return string

def qr_display_unique(unit):
    set1={unit}
    for i in set1:
        return str(i)
def qrdisplay(barcodeData,barcodeType):
    print("Barcode: " + barcodeData + " | Type: " + barcodeType)
    if url_data.url_validator(qr_display_unique(barcodeData)) == 'T':
        url_data.url_opener(qr_display_unique(barcodeData))