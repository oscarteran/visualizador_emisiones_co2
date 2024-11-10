# Guía de Contribución

## Índice
- [¿Cómo puedo contribuir?](#cómo-puedo-contribuir)
- [Pull Requests](#pull-requests)
- [Estilo de Código](#estilo-de-código)
- [Reporte de Bugs](#reporte-de-bugs)


## ¿Cómo puedo contribuir?

1. Haz un Fork del repositorio
2. Crea una rama para tu contribución:
```bash
git checkout -b feature/NombreDeTuFeature
```
Realiza tus cambios y documéntalos
Asegúrate de que los tests pasen (si existen)
Haz commit de tus cambios:

```bash
git commit -m "feat: Descripción concisa del cambio"
```

Sube tus cambios a tu fork:

```bash
git push origin feature/NombreDeTuFeature
```

Abre un Pull Request

## Pull Requests
Guía para crear un Pull Request

Asegúrate de que tu PR incluya:

- Una descripción clara del objetivo
- Referencias a issues relacionados
- Capturas de pantalla (si aplica)


La descripción debe seguir esta plantilla:

```markdown
## Descripción
[Descripción detallada de los cambios]

## Tipo de cambio
- [ ] Bugfix
- [ ] Feature
- [ ] Mejora de código
- [ ] Documentación

## ¿Cómo se ha probado?
[Descripción de las pruebas realizadas]

## Checklist
- [ ] Mi código sigue las guías de estilo del proyecto
- [ ] He comentado mi código donde es necesario
- [ ] He actualizado la documentación
- [ ] Los tests pasan localmente
```

## Estilo de Código

- Sigue las convenciones de estilo existentes
- Usa nombres descriptivos para variables y funciones
- Comenta el código cuando sea necesario
- Sigue la guía de estilo de Python (PEP 8)

Convenciones de Commits
Usamos Conventional Commits:

- `feat`: Nueva característica
- `fix`: Corrección de bug
- `docs`: Cambios en documentación
- `style`: Cambios de formato
- `refactor`: Refactorización de código
- `test`: Añadir o modificar tests
- `chore`: Tareas de mantenimiento

Ejemplo:
```bash
feat: Añadir validación de entrada de usuario
```

## Reporte de Bugs
Antes de Reportar

- Busca en los issues existentes
- Verifica que estés usando la última versión

### Cómo Reportar
Abre un issue incluyendo:

- Descripción clara del problema
- Pasos para reproducir
- Comportamiento esperado
- Comportamiento actual
- Capturas de pantalla (si aplica)
- Entorno (OS, versión de Python, etc.)

Plantilla para Bugs
```markdown
## Descripción del Bug
[Descripción clara y concisa]

## Pasos para Reproducir
1. Ir a '...'
2. Click en '....'
3. Scroll hasta '....'
4. Ver error

## Comportamiento Esperado
[Descripción]

## Comportamiento Actual
[Descripción]

## Capturas de Pantalla
[Si aplica]

## Entorno
 - OS: [ej. Windows 10]
 - Python Version: [ej. 3.8.0]
 - Versiones de dependencias relevantes
```
Notas Adicionales

- Asegúrate de tener los tests actualizados
- Mantén los cambios enfocados y pequeños
- Documenta los cambios significativos
- Sigue las mejores prácticas de seguridad