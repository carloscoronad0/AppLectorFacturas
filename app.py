from controller.control_facturas import ControlFacturas

def main():
    fac_control = ControlFacturas('Testiing')
    try:
        fac_control.add_from_folder("./FacturasTesteo")
        fac_control.write_to_file("Test.csv")
    except Exception as inst:
        print(inst)

if __name__ == '__main__':
    main()
