# Archivos Estáticos - Shoppyco

Esta carpeta contiene los archivos estáticos CSS para la aplicación Shoppyco.

## Estructura de Archivos

```
static/
├── css/
│   ├── custom.css          # Estilos principales de la aplicación
│   └── products.css        # Estilos específicos para páginas de productos

```

## Archivos CSS

### custom.css
Contiene los estilos principales de la aplicación:
- Variables CSS (colores, fuentes, etc.)
- Estilos de navegación
- Estilos de hero section
- Estilos de cards y botones
- Estilos de tablas
- Estilos de footer
- Media queries para responsividad

### products.css
Contiene estilos específicos para las páginas de productos:
- Estilos de headers de página
- Estilos de grids de productos
- Estados vacíos
- Tarjetas de estadísticas

## Uso en Templates

### Template Base (index.html)
```html
<!-- CSS -->
<link rel="stylesheet" href="{% static 'css/custom.css' %}">
{% block extra_css %}{% endblock %}
```

### Templates de Productos
```html
{% block extra_css %}
    <link rel="stylesheet" href="{% static 'css/products.css' %}">
{% endblock %}
```

## Características

- **Responsivo**: Todos los estilos están optimizados para dispositivos móviles
- **Moderno**: Usa CSS Grid, Flexbox y variables CSS
- **Simple**: Solo estilos CSS puros, sin JavaScript complejo
- **Organizado**: Estilos separados por funcionalidad

## Dependencias Externas

- Bootstrap 5.3.2 (CDN)
- Bootstrap Icons 1.11.1 (CDN)
- Google Fonts - Inter (CDN)

## Notas de Desarrollo

- Los estilos están organizados por funcionalidad
- Se usan variables CSS para consistencia de colores
- Los media queries están al final de cada archivo
- Solo CSS puro, sin funcionalidades JavaScript complejas
