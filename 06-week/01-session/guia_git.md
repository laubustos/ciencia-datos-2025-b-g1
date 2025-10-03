# Guía básica de Git

## Clonar repositorio
```bash
git clone <enlace>
```
Explicación: Descarga una copia local del repositorio remoto (por ejemplo, en GitHub o GitLab).  
`<enlace>` corresponde a la URL del repositorio.

---

## Obtener cambios
```bash
git pull
```
Explicación: Actualiza la copia local trayendo los cambios más recientes del repositorio remoto.  
Une automáticamente la rama remota con tu rama local.

---

## Publicar cambios
```bash
git pull
git add .
git commit -m "mensaje de cambios"
git push
git pull
```

- `git pull` → Primero aseguras que tu rama local está actualizada con el remoto.  
- `git add .` → Agrega **todos** los archivos modificados al área de preparación (staging).  
- `git commit -m "mensaje de cambios"` → Confirma los cambios con un mensaje descriptivo.  
- `git push` → Envía los cambios confirmados al repositorio remoto.  
- `git pull` (final) → Verifica que tu repositorio local sigue sincronizado después del push.
