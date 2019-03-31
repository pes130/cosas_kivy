# Ejemplo de aplicación
Una cosa destacable de este ejemplo, es que redefinimos un nuevo Layout a partir de un GridLayout. Esto es debido a que vamos a añadirle más funcionalidad y atributos. Más adelante, conforme sea necesario, veremos cómo hacerlo.

El código de la aplicación queda así de sencillo:
```python
class CalcGridLayout(GridLayout):
    pass

class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()


calcApp = CalculatorApp()
calcApp.run()
```
Por lo pronto, el código de la clase **CalcGridLayout** lo dejamos vacío. 

Respecto a **calculator.kv**:
```yaml
<CustButton@Button>:
    font_size: 32

<CalcGridLayout>:
    id: calculator
    mi_display: entry
    rows: 5
    padding: 10
    spacing: 10
    
    BoxLayout:
        TextInput:
            id: entry
            font_size: 32
            multiline: False

    BoxLayout:
        spacing: 10
        CustButton:
            text: "7"
            on_press: entry.text += self.text
        CustButton:
            text: "8"
            on_press: entry.text += self.text
        CustButton:
            text: "9"
            on_press: entry.text += self.text
        CustButton:
            text: "+"
            on_press: entry.text += self.text

    BoxLayout:
        spacing: 10
        CustButton:
            text: "5"
            on_press: entry.text += self.text
        CustButton:
            text: "6"
            on_press: entry.text += self.text
        CustButton:
            text: "7"
            on_press: entry.text += self.text
        CustButton:
            text: "-"
            on_press: entry.text += self.text

    BoxLayout:
        spacing: 10
        CustButton:
            text: "1"
            on_press: entry.text += self.text
        CustButton:
            text: "2"
            on_press: entry.text += self.text
        CustButton:
            text: "3"
            on_press: entry.text += self.text
        CustButton:
            text: "*"
            on_press: entry.text += self.text

    BoxLayout:
        spacing: 10
        CustButton:
            text: "AC"
        CustButton:
            text: "0"
            on_press: entry.text += self.text
        CustButton:
            text: "="
        CustButton:
            text: "/"
            on_press: entry.text += self.text
```

A tener en cuenta:
* Definimos el botón ***CustButton*** partiendo de Button. Se trata del botón que usaremos como teclas de la calculadora y trendrás todos un tamaño de letra de 32 puntos.
* Nuestro ***CalGridLayout*** es un GridLayout con 5 filas. 
    * En la primera fila pintaremos la pantalla (una caja de texto)
    * En la segunda las teclas 7, 8, 9 y +
    * En la tercera las teclas 4, 5, 6 y -
    * En la cuarta, 1, 2, 3, y *
    * En la última AC, 0, = y /
* Además, en ***CalcGridLayout*** hemos especificado:
    * **id: calculator** --> identificador único para un componente. Nombre que se le dará a la instancia creada de la clase CalcGridLayout. Esto nos permitirá referirnos, desde el fichero kv la instancias de los objetos que hemos creado. Lo veremos más adelante.
    * **padding: 10** --> Espacio entre los bordes del layout y sus hijos. Puede descomponerse en *padding_left*, *padding_top*, *padding_right* y *padding_bottom*. También *padding_horizontal* y *padding_vertical*.
    * **spacing: 10** --> Espacio entre los hijos del layout. Puedes descomponerlo en *spacing_horizontal* y *spacing_vertical*.
    * **mi_display: entry** --> se trata de una propiedad o atributo personalizado que le hemos añadido a CustGridLayout. Su valor es el id de la caja de texto (*TextInput*) donde se van pintando los números. Desde el .py, podemos hacer referencia a esa propiedad así: *self.mi_display.text*.

Para cada uno de los botones añadidos, definimos su texto mediante la propiedad **text**.

Además, programamos su comportamiento, lo que ocurre en el evento clic, con la propiedad **on_press**.

Para casi todos, esta propiedad es:
```yaml
on_press: entry.text += self.text
```
Es decir, al TextInput con id *entry*, le concatenamos el texto del botón pulsado.

La cosa cambia con el botón '=', que deberá hacer un eval de la operación que tenemos en *entry*. Lo hacemos de la siguiente manera: en el kv, estaríamos metiendo ya lógica, así que para evitarlo, hacemos así:
```yaml
CustButton:
    text: "="
    on_press: calculator.calculate(entry.text)
```

Y ahora, en **main.py**:
```python
def calculate(self, calculation):
    if calculation:
        try:
            self.mi_display.text = str(eval(calculation))
        except Exception:
            self.mi_display.text = "Error"
``` 

