import bpy
import os

paths = os.listdir("/tmp/objs")
paths.sort()

print(paths)

for path in paths:
    temp_path = "/tmp/objs/" + path
    bpy.ops.import_scene.obj(filepath=temp_path, axis_forward='Y', axis_up='Z')

objects = list(bpy.data.objects)
for object in objects:
    if not bpy.data.meshes.get(object.name):
        continue
    object.hide_viewport = True
    object.hide_render = True
    
frame = 1.0
for object in objects:
    if not bpy.data.meshes.get(object.name):
        continue
    bpy.context.view_layer.objects.active = object
    bpy.context.active_object.keyframe_insert(data_path = "hide_render", frame = frame - 1.0)
    bpy.context.active_object.keyframe_insert(data_path = "hide_viewport", frame = frame - 1.0)
    bpy.context.view_layer.objects.active.hide_render = False
    bpy.context.view_layer.objects.active.hide_viewport = False
    bpy.context.active_object.keyframe_insert(data_path = "hide_render", frame = frame)
    bpy.context.active_object.keyframe_insert(data_path = "hide_viewport", frame = frame)
    bpy.context.view_layer.objects.active.hide_render = True
    bpy.context.view_layer.objects.active.hide_viewport = True
    bpy.context.active_object.keyframe_insert(data_path = "hide_render", frame = frame + 1.0)
    bpy.context.active_object.keyframe_insert(data_path = "hide_viewport", frame = frame + 1.0)
    bpy.context.active_object.show_wire = True
    frame += 1.0

bpy.data.scenes['Scene'].frame_end = frame
bpy.data.scenes['Scene'].frame_current = 1.0
