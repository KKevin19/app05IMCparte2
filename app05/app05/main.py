import flet as ft

def calcilar_imc(txtPeso,txtAltura,lblIMC,page):
    try:
        peso=float(txtPeso.value)
        altura=float(txtAltura.value)
        imc=peso/(altura**2)
        lblIMC.value=f"tu IMC es: {imc:.2f}"
        page.update()
        
    #funcion para cerrar el cuadoro de dialogo
    def cerrar_dialogo():
        page.dialog.open=False
        page.update()

#validar condiciones del IMC    
if imc<18.5:
    dialog = ft.AlertDialog(
        title=ft.text("Resultado de IMC"),
        content=ft.text("Actualmente estas bajo de peso"),
        action=[ft.TextButton("OK", on_click=cerrar_dialogo)],
    )       
    
elif imc<18.5 and imc < 24.9:
    dialog = ft.AlertDialog(
        title=ft.text("Resultado de IMC"),
        content=ft.text("tu peso es normal"),
        action=[ft.TextButton("OK", on_click=cerrar_dialogo)],
    )    
    
elif imc >= 25 and imc <30:
    dialog = ft.AlertDialog(
        title=ft.text("Resultado de IMC"),
        content=ft.text("tienes sobre peso"),
        action=[ft.TextButton("OK", on_click=cerrar_dialogo)],
    )    
else:
    dialog = ft.AlertDialog(
        title=ft.text("Resultado de IMC"),
        content=ft.text("tienes sobre peso"),
        action=[ft.TextButton("OK", on_click=cerrar_dialogo)],
    )    
    
    except ValueError:    

def cerrar_dialogo(e):
    page.dialog.open=False
    pagex.update()
    
    dialog=ft.alert_dialog(
        title=ft.Text("Error"),
        content=ft.Text("Debes ingresar valores numericos"),
        actions=[ft.TextButton("OK",on_click=cerrar_dialogo)]
    )

    page.dialog.open=dialog
    pagex.update()
    
def main(page: ft.Page):
    page.title = "calculadora de IMC"
    page.bgcolor="purple"
    
    txtpeso=ft.TextField(label="ingresa tu peso")
    txtAltura=ft.TextField(label="ingresa tu altura")
    lblIMC=ft.Text("tu IMC es: ")
    
    img=ft.Image(src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
                width=200,
                height=200
                
                )
    
    
    def on_calcular_click(e):
        calcular_imc(txtpeso,txtAltura,lblIMC,page)
    
    btnCalcular=ft.ElevatedButton(text="calcular",on_click=on_alcular_click)
    btnlimpiar=ft.ElevatedButton(text="limpiar",on_click=limpiar)
    
    
    page.add(
        ft.Column(
            controls=[txtpeso,
                    txtAltura,
                    lblIMC
                    ],alignment="CENTER"),
        ft.Row(
            controls=[
                img
            ],alignment="CENTER"),
        ft.Row(
            controls=[
                btnCalcular,
                btnlimpiar
            ],alignment="CENTER")
        )    
    

ft.app(target=main,view=ft.AppView.WEB_BROWSER)