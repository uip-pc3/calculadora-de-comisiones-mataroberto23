from flask import Flask, render_template, request

def guardar(dato):
    with open('Comision.csv', 'a+') as archivo:
        for item in dato:
            archivo.write(item+",")
        archivo.write('\n')
    archivo.close()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def mostrar_comision():
    nombre = request.form['nombre'].strip()
    apellido = request.form['apellido'].strip()
    venta = request.form['venta'].strip()

    if apellido != '' and nombre != '' and venta != '':
        venta = int(venta)
        if venta > 100000:  comision = 15
        elif venta > 75000: comision = 10
        elif venta > 50000: comision = 7
        elif venta > 25000: comision = 5
        elif venta > 0:     comision = 3
        else:
            mensaje ="debe realizar mas ventas"
            return render_template('comision.html', nombre=nombre, apellido=apellido, venta=venta,  msg =mensaje)

        # Calculo de comision
        comision = venta * (comision / 100)

        datos = [apellido,nombre,str(venta),str(comision)]
        # Guardamos los datos el erchivo
        guardar(datos)

        return render_template('comision.html', nombre=nombre, apellido=apellido, venta=venta, comision=comision)
    else:
        return render_template('home.html', error="Error ingrese datos validos")


if __name__ == '__main__':
    app.run()