bpy.context.scene.objects.get("Passive").select_set(True)
bpy.context.view_layer.objects.active = bpy.context.scene.objects.get("Passive")
bpy.ops.object.join()
bpy.ops.screen.frame_jump(end=False)
bpy.ops.object.select_pattern(pattern="Cube*", extend=False)
bpy.ops.object.duplicate_move()
bpy.ops.stb.scriptbutton(btn_name="Object Random Loc")
bpy.ops.stb.scriptbutton(btn_name="PlayAnim3")