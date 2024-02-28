#! /usr/bin/env python3

# import os

# for i in range (0,30):
#         os.system("rosrun ar_track_alvar createMarker {0}".format(i))
#         fn = "ar_tag_{0}.png".format(i)
#         os.system("convert {0} -bordercolor white -border 100x100 {0}".format(fn))
#         with open("product_{0}.material".format(i), 'w') as f:
#                 f.write("""
#                         material product_%d {
#                         receive_shadows on 
#                         technique{
#                             pass{
#                                 ambient 1 1 1 1
#                                 diffuse 1 1 1 1
#                                 specular 0.5 0.5 0.5 1
#                                 lighting on
#                                 shading gouraud
#                                 texture_unit { texture MarkerData_%d.png }
#                                }
#                             }
#                         }
#                     """ % (i,i))


# import os
# import subprocess


# def add_border_to_image(image_path, border_size):
#     with Image.open(image_path) as img:
#         width, height = img.size
#         new_width = width + 2 * border_size
#         new_height = height + 2 * border_size

#         # Create a new image with white background
#         new_img = Image.new("RGB", (new_width, new_height), "white")
#         new_img.paste(img, (border_size, border_size))

#         new_img.save(image_path)

# def generate_ar_tags(start_id, end_id, size, border_size, output_dir):
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)

#     for tag_id in range(start_id, end_id + 1):
#         tag_filename = f"MarkerData_{tag_id}_0.png"
#         model_dir = os.path.join(output_dir, f"model_tag_{tag_id}")
#         os.makedirs(model_dir, exist_ok=True)

#         # Generate AR tag
#         subprocess.run(["rosrun", "ar_track_alvar", "createMarker", str(tag_id), tag_filename])

#         # Add border
#         add_border_to_image(tag_filename, border_size)

#         # Move the tag to the model directory
#         os.rename(tag_filename, os.path.join(model_dir, tag_filename))

#         # Create Gazebo model files
#         with open(os.path.join(model_dir, "model.sdf"), "w") as sdf_file:
#             sdf_file.write(create_sdf_content(tag_filename, size))

#         with open(os.path.join(model_dir, "model.config"), "w") as config_file:
#             config_file.write(create_config_content(f"AR Tag {tag_id}"))

# def create_sdf_content(image_name, size):
#     size_meter = size / 100  # Convert cm to meters
#     return f"""<?xml version="1.0" ?>
# <sdf version="1.4">
#   <model name="ar_tag">
#     <static>true</static>
#     <link name="link">
#       <visual name="visual">
#         <geometry>
#           <box>
#             <size>{size_meter} {size_meter} 0.001</size>
#           </box>
#         </geometry>
#         <material>
#           <script>
#             <uri>file://{image_name}</uri>
#             <name>{image_name}</name>
#           </script>
#         </material>
#       </visual>
#     </link>
#   </model>
# </sdf>
# """

# def create_config_content(model_name):
#     return f"""<?xml version="1.0"?>
# <model>
#   <name>{model_name}</name>
#   <version>1.0</version>
#   <sdf version="1.4">model.sdf</sdf>
#   <author>
#    <name>Your Name</name>
#    <email>your.email@example.com</email>
#   </author>
#   <description>
#     AR Tag for Gazebo
#   </description>
# </model>
# """

# if __name__ == "__main__":
#     generate_ar_tags(0, 1, 8, 40, "ar_tags_gazebo_models")


import os
import subprocess
from PIL import Image

def generate_ar_tags_with_border(start_id, end_id, size, border_size, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
   

    for tag_id in range(start_id, end_id + 1):
        tag_filename = f"MarkerData_{tag_id}_0.png"
        model_dir = os.path.join(output_dir, f"model_tag_{tag_id}")
        os.makedirs(model_dir, exist_ok=True)

        if not os.path.exists(model_dir + "/meshes"):
            os.makedirs(model_dir + "/meshes")

        meshes_dir = os.path.join(model_dir, "meshes")
        os.makedirs(meshes_dir, exist_ok=True)

        # Generate AR tag
        subprocess.run(["rosrun", "ar_track_alvar", "createMarker", str(tag_id), tag_filename])

        # Add border
        add_border_to_image(tag_filename, border_size)

        # Move the tag to the model directory
        os.rename(tag_filename, os.path.join(model_dir, tag_filename))

        
        # Create Gazebo model files
        with open(os.path.join(model_dir, "model.sdf"), "w") as sdf_file:
            sdf_file.write(create_sdf_content(tag_id, size))

        with open(os.path.join(model_dir, "model.config"), "w") as config_file:
            config_file.write(create_config_content(f"AR Tag {tag_id}"))
        
        with open(os.path.join(meshes_dir, "marker.dae"), "w") as config_file:
            config_file.write(create_dae_content(tag_id))

def create_sdf_content(tag_id, size):
    size_meter = size / 100  # Convert cm to meters
    return f"""
<?xml version="1.0" ?><sdf version="1.6">
  <model name="ar_tag_{tag_id}">
    <static>true</static>
    <link name="link">
      <visual name="visual">
        <geometry>
          <mesh>
            <uri>model://model_tag_{tag_id}/meshes/marker.dae</uri>
          <scale>0.2 0.2 0.2</scale>
          </mesh>
        </geometry>
      </visual>
    </link>
  </model>
</sdf>
"""

def create_config_content(model_name):
    return f"""<?xml version="1.0"?>
<model>
  <name>{model_name}</name>
  <version>1.0</version>
  <sdf version="1.6">model.sdf</sdf>
  <author>
   <name>Your Name</name>
   <email>your.email@example.com</email>
  </author>
  <description>
    AR Tag for Gazebo
  </description>
</model>
"""

def create_dae_content(tag_id):
    return f"""<?xml version="1.0" ?><COLLADA xmlns="http://www.collada.org/2005/11/COLLADASchema" version="1.4.1">
    <asset>
      <contributor>
        <author>Blender User</author>
        <authoring_tool>Blender 2.74.0 commit date:2015-03-31, commit time:13:39, hash:000dfc0</authoring_tool>
      </contributor>
      <created>2015-04-05T02:03:25</created>
      <modified>2015-04-05T02:03:25</modified>
      <unit name="meter" meter="1"/>
      <up_axis>Z_UP</up_axis>
    </asset>
    <library_images>
      <image id="Marker_Data_{tag_id}_0_png" name="Marker_Data_{tag_id}_0_png">
        <init_from>Marker_Data_{tag_id}_0.png</init_from>
      </image>
    </library_images>
    <library_effects>
      <effect id="Marker_Data_{tag_id}_0Mat-effect">
        <profile_COMMON>
          <newparam sid="Marker_Data_{tag_id}_0_png-surface">
            <surface type="2D">
              <init_from>Marker_Data_{tag_id}_0_png</init_from>
            </surface>
          </newparam>
          <newparam sid="Marker_Data_{tag_id}_0_png-sampler">
            <sampler2D>
              <source>Marker_Data_{tag_id}_0_png-surface</source>
            </sampler2D>
          </newparam>
          <technique sid="common">
            <phong>
              <emission>
                <color sid="emission">0 0 0 1</color>
              </emission>
              <ambient>
                <color sid="ambient">0.9 0.9 0.9 1</color>
              </ambient>
              <diffuse>
                <texture texture="Marker_Data_{tag_id}_0_png-sampler" texcoord="UVMap"/>
              </diffuse>
              <specular>
                <color sid="specular">0.5 0.5 0.5 1</color>
              </specular>
              <shininess>
                <float sid="shininess">50</float>
              </shininess>
              <index_of_refraction>
                <float sid="index_of_refraction">1</float>
              </index_of_refraction>
            </phong>
          </technique>
        </profile_COMMON>
      </effect>
    </library_effects>
    <library_materials>
      <material id="Marker_Data_{tag_id}_0Mat-material" name="Marker_Data_{tag_id}_0Mat">
        <instance_effect url="#Marker_Data_{tag_id}_0Mat-effect"/>
      </material>
    </library_materials>
    <library_geometries>
      <geometry id="Cube-mesh" name="Cube">
        <mesh>
          <source id="Cube-mesh-positions">
            <float_array id="Cube-mesh-positions-array" count="24">1 0.9999999 -9.41753e-6 1 -1 -9.41753e-6 -1 -0.9999998 -9.41753e-6 -0.9999997 1 -9.41753e-6 1 0.9999994 1.999991 0.9999994 -1.000001 1.999991 -1 -0.9999997 1.999991 -0.9999999 1 1.999991</float_array>
            <technique_common>
              <accessor source="#Cube-mesh-positions-array" count="8" stride="3">
                <param name="X" type="float"/>
                <param name="Y" type="float"/>
                <param name="Z" type="float"/>
              </accessor>
            </technique_common>
          </source>
          <source id="Cube-mesh-normals">
            <float_array id="Cube-mesh-normals-array" count="36">0 0 -1 0 0 1 1 -5.66244e-7 3.27825e-7 -4.76837e-7 -1 0 -1 2.38419e-7 -1.19209e-7 2.38419e-7 1 1.78814e-7 0 0 -1 0 0 1 1 0 -2.38419e-7 0 -1 -2.98023e-7 -1 2.38419e-7 0 2.98023e-7 1 2.38418e-7</float_array>
            <technique_common>
              <accessor source="#Cube-mesh-normals-array" count="12" stride="3">
                <param name="X" type="float"/>
                <param name="Y" type="float"/>
                <param name="Z" type="float"/>
              </accessor>
            </technique_common>
          </source>
          <source id="Cube-mesh-map-0">
            <float_array id="Cube-mesh-map-0-array" count="72">0 0 0 0 0 0 0 0 0 0 0 0 0.9999 0.9940189 9.96856e-5 0.9940189 1.00079e-4 9.97642e-5 0 0 0 0 0 0 9.96856e-5 0.9940191 9.98823e-5 9.96856e-5 0.9999004 9.98429e-5 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.9999004 9.96856e-5 0.9999 0.9940189 1.00079e-4 9.97642e-5 0 0 0 0 0 0 0.9999004 0.9940191 9.96856e-5 0.9940191 0.9999004 9.98429e-5 0 0 0 0 0 0</float_array>
            <technique_common>
              <accessor source="#Cube-mesh-map-0-array" count="36" stride="2">
                <param name="S" type="float"/>
                <param name="T" type="float"/>
              </accessor>
            </technique_common>
          </source>
          <vertices id="Cube-mesh-vertices">
            <input semantic="POSITION" source="#Cube-mesh-positions"/>
          </vertices>
          <polylist material="Marker_Data_{tag_id}_0Mat-material" count="12">
            <input semantic="VERTEX" source="#Cube-mesh-vertices" offset="0"/>
            <input semantic="NORMAL" source="#Cube-mesh-normals" offset="1"/>
            <input semantic="TEXCOORD" source="#Cube-mesh-map-0" offset="2" set="0"/>
            <vcount>3 3 3 3 3 3 3 3 3 3 3 3 </vcount>
            <p>0 0 0 1 0 1 2 0 2 7 1 3 6 1 4 5 1 5 4 2 6 5 2 7 1 2 8 5 3 9 6 3 10 2 3 11 2 4 12 6 4 13 7 4 14 0 5 15 3 5 16 7 5 17 3 6 18 0 6 19 2 6 20 4 7 21 7 7 22 5 7 23 0 8 24 4 8 25 1 8 26 1 9 27 5 9 28 2 9 29 3 10 30 2 10 31 7 10 32 4 11 33 0 11 34 7 11 35</p>
          </polylist>
        </mesh>
      </geometry>
    </library_geometries>
    <library_controllers/>
    <library_visual_scenes>
      <visual_scene id="Scene" name="Scene">
        <node id="Marker_Data_{tag_id}_0" name="Marker_Data_{tag_id}_0" type="NODE">
          <matrix sid="transform">0.004999998 0 0 0 0 0.2499999 0 0 0 0 0.25 0 0 0 0 1</matrix>
          <instance_geometry url="#Cube-mesh">
            <bind_material>
              <technique_common>
                <instance_material symbol="Marker_Data_{tag_id}_0Mat-material" target="#Marker_Data_{tag_id}_0Mat-material">
                  <bind_vertex_input semantic="UVMap" input_semantic="TEXCOORD" input_set="0"/>
                </instance_material>
              </technique_common>
            </bind_material>
          </instance_geometry>
        </node>
      </visual_scene>
    </library_visual_scenes>
    <scene>
      <instance_visual_scene url="#Scene"/>
    </scene>
  </COLLADA>
"""



def add_border_to_image(image_path, border_size):
    with Image.open(image_path) as img:
        width, height = img.size
        new_width = width + 2 * border_size
        new_height = height + 2 * border_size

        # Create a new image with white background
        new_img = Image.new("RGB", (new_width, new_height), "white")
        new_img.paste(img, (border_size, border_size))

        new_img.save(image_path)

# Main execution
if __name__ == "__main__":
    generate_ar_tags_with_border(1, 10, 8, 40, "ar_tags_gazebo_models")  # 10 is the border size in pixels
