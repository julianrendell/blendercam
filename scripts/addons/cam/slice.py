# blender CAM slice.py (c) 2021 Alain Pelletier
#
# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****

#very simple slicing for 3d meshes, usefull for plywood cutting.
#completely rewritten April 2021

import bpy

def slicing(ob,height): #April 2020 Alain Pelletier
	#let's slice things
	bpy.ops.object.mode_set(mode = 'EDIT')		#force edit mode
	bpy.ops.mesh.select_all(action='SELECT')	#select all vertices
	#actual slicing here
	bpy.ops.mesh.bisect(plane_co=(0.0, 0.0, height), plane_no=(0.0, 0.0, 1.0), use_fill=True, clear_inner=True, clear_outer=True) 
	#slicing done
	bpy.ops.object.mode_set(mode = 'OBJECT')	#force object mode
	#bring all the slices to 0 level and reset location transform
	ob.location[2] = -1*height
	bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)
	bpy.ops.object.convert(target='CURVE') 		#convert it to curve
	if bpy.context.active_object.type != 'CURVE':  #conversion failed because mesh was empty so delete mesh
	    bpy.ops.object.delete(use_global=False, confirm=False)		
	bpy.ops.object.select_all(action='DESELECT')	#deselect everything

def sliceObject(ob):   #April 2020 Alain Pelletier
	#setup the collections
	thickness=bpy.context.scene.cam_slice.slice_distance
	scollection = bpy.data.collections.new("Slices")
	tcollection = bpy.data.collections.new("Text")
	bpy.context.scene.collection.children.link(scollection)
	bpy.context.scene.collection.children.link(tcollection)

	#show object information
	print(ob.dimensions)
	print(ob.location)

	layeramt=int(ob.dimensions.z // thickness)	#calculate amount of layers needed
	
	bpy.ops.object.mode_set(mode = 'OBJECT')	#force object mode

	for layer in range(layeramt):
		height=round(layer*thickness,6)		#height of current layer
		t=str(layer)+"-"+str(height*1000)
		slicename="slice-"+t	#name for the current slice
		tslicename="t-" + t		#name for the current slice text
		print(slicename)

		#text objects
		bpy.ops.object.text_add()			#new text object
		textob = bpy.context.active_object
		textob.data.size = 0.006			#change size of object
		textob.data.body = t				#text content
		textob.location=(0,0,0)				#text location
		bpy.ops.object.select_all(action='DESELECT') #deselect everything
		tcollection.objects.link(textob)	#add to text collection
		
		ob.select_set(True)					#select object to be sliced
		bpy.context.view_layer.objects.active = ob #make object to be sliced active
		bpy.ops.object.duplicate()			#make a copy of object to be sliced
		bpy.context.view_layer.objects.active.name = slicename  #change the name of object
		
		obslice=bpy.context.view_layer.objects.active	#attribute active object to obslice
		scollection.objects.link(obslice)				#link obslice to scollecton
		
		slicing(obslice,height)		#slice object at desired height
	# select all curve slices
	for obj in bpy.data.collections['Slices'].all_objects: obj.select_set(True)


