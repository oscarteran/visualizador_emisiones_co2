# Formas de Escribir Texto en Streamlit

En Streamlit, tienes varias opciones para mostrar texto con diferentes estilos y formatos.

## 1. Encabezados y Texto con Formato Básico
- `st.title("Título")` → Título principal (similar a un encabezado H1).
- `st.header("Encabezado")` → Encabezado secundario (similar a H2).
- `st.subheader("Subencabezado")` → Subencabezado (similar a H3).
- `st.caption("Texto de pie de foto")` → Texto pequeño para comentarios o pies de foto.
- `st.text("Texto simple")` → Muestra texto en formato básico, sin estilo adicional.
- `st.markdown("Texto en Markdown")` → Permite usar Markdown para dar formato al texto (negrita, cursiva, enlaces, listas, etc.).

## 2. Texto Enriquecido con Markdown
Streamlit soporta Markdown, así que puedes utilizarlo para:

- **Negrita**: `**negrita**`
- *Cursiva*: `*cursiva*`
- **Encabezados**: `# H1`, `## H2`, `### H3`, etc.
- Listas: `- Elemento de lista` o `1. Elemento numerado`
- Enlaces: `[texto del enlace](https://link.com)`
- Bloques de código: 
  ```python
  print("Hola, Streamlit")
  ```

## 3. Texto con Estilo HTML
Streamlit con st.markdown también soporta algunos elementos HTML:

 ```python
st.markdown("<h1 style='color:blue;'>Texto en azul</h1>", unsafe_allow_html=True)
 ```

Al utilizar unsafe_allow_html=True, tienes flexibilidad en estilos CSS y algunas etiquetas HTML.

## 4. Código

 ```python 
 st.code("print('Hola, Streamlit')", language="python") 
 ```
→ Muestra código con formato resaltado según el lenguaje especificado.


## 5. Otros Estilos Específicos
  ```python
  st.latex(r"e^{i\pi} + 1 = 0")
  ```  
 → Para mostrar expresiones matemáticas en LaTeX.


  ```python
  st.write("Texto o expresión")
  ``` 
 → Método versátil que detecta automáticamente el tipo de contenido (texto, Markdown, LaTeX, etc.).

Con estas opciones, puedes crear texto con el formato y estilo que necesites en Streamlit.

Este archivo `.md` contiene toda la información que necesitas para documentar las distintas formas de escribir texto en Streamlit.
