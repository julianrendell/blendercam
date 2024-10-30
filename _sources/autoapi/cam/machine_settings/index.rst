cam.machine_settings
====================

.. py:module:: cam.machine_settings

.. autoapi-nested-parse::

   BlenderCAM 'machine_settings.py'

   All CAM machine properties.



Classes
-------

.. autoapisummary::

   cam.machine_settings.machineSettings


Module Contents
---------------

.. py:class:: machineSettings

   Bases: :py:obj:`bpy.types.PropertyGroup`


   stores all data for machines


   .. py:attribute:: post_processor
      :type:  EnumProperty(name='Post Processor', items=(('ISO', 'Iso', 'Exports standardized gcode ISO 6983 (RS-274)'), ('MACH3', 'Mach3', 'Default mach3'), ('EMC', 'LinuxCNC - EMC2', 'Linux based CNC control software - formally EMC2'), ('FADAL', 'Fadal', 'Fadal VMC'), ('GRBL', 'grbl', 'Optimized gcode for grbl firmware on Arduino with cnc shield'), ('HEIDENHAIN', 'Heidenhain', 'Heidenhain'), ('HEIDENHAIN530', 'Heidenhain530', 'Heidenhain530'), ('TNC151', 'Heidenhain TNC151', 'Post Processor for the Heidenhain TNC151 machine'), ('SIEGKX1', 'Sieg KX1', 'Sieg KX1'), ('HM50', 'Hafco HM-50', 'Hafco HM-50'), ('CENTROID', 'Centroid M40', 'Centroid M40'), ('ANILAM', 'Anilam Crusader M', 'Anilam Crusader M'), ('GRAVOS', 'Gravos', 'Gravos'), ('WIN-PC', 'WinPC-NC', 'German CNC by Burkhard Lewetz'), ('SHOPBOT MTC', 'ShopBot MTC', 'ShopBot MTC'), ('LYNX_OTTER_O', 'Lynx Otter o', 'Lynx Otter o')), description='Post Processor', default='MACH3')


   .. py:attribute:: use_position_definitions
      :type:  BoolProperty(name='Use Position Definitions', description='Define own positions for op start, toolchange, ending position', default=False)


   .. py:attribute:: starting_position
      :type:  FloatVectorProperty(name='Start Position', default=(0, 0, 0), unit='LENGTH', precision=constants.PRECISION, subtype='XYZ', update=updateMachine)


   .. py:attribute:: mtc_position
      :type:  FloatVectorProperty(name='MTC Position', default=(0, 0, 0), unit='LENGTH', precision=constants.PRECISION, subtype='XYZ', update=updateMachine)


   .. py:attribute:: ending_position
      :type:  FloatVectorProperty(name='End Position', default=(0, 0, 0), unit='LENGTH', precision=constants.PRECISION, subtype='XYZ', update=updateMachine)


   .. py:attribute:: working_area
      :type:  FloatVectorProperty(name='Work Area', default=(0.5, 0.5, 0.1), unit='LENGTH', precision=constants.PRECISION, subtype='XYZ', update=updateMachine)


   .. py:attribute:: feedrate_min
      :type:  FloatProperty(name='Feedrate Minimum /min', default=0.0, min=1e-05, max=320000, precision=constants.PRECISION, unit='LENGTH')


   .. py:attribute:: feedrate_max
      :type:  FloatProperty(name='Feedrate Maximum /min', default=2, min=1e-05, max=320000, precision=constants.PRECISION, unit='LENGTH')


   .. py:attribute:: feedrate_default
      :type:  FloatProperty(name='Feedrate Default /min', default=1.5, min=1e-05, max=320000, precision=constants.PRECISION, unit='LENGTH')


   .. py:attribute:: hourly_rate
      :type:  FloatProperty(name='Price per Hour', default=100, min=0.005, precision=2)


   .. py:attribute:: spindle_min
      :type:  FloatProperty(name='Spindle Speed Minimum RPM', default=5000, min=1e-05, max=320000, precision=1)


   .. py:attribute:: spindle_max
      :type:  FloatProperty(name='Spindle Speed Maximum RPM', default=30000, min=1e-05, max=320000, precision=1)


   .. py:attribute:: spindle_default
      :type:  FloatProperty(name='Spindle Speed Default RPM', default=15000, min=1e-05, max=320000, precision=1)


   .. py:attribute:: spindle_start_time
      :type:  FloatProperty(name='Spindle Start Delay Seconds', description='Wait for the spindle to start spinning before starting the feeds , in seconds', default=0, min=0.0, max=320000, precision=1)


   .. py:attribute:: axis4
      :type:  BoolProperty(name='#4th Axis', description='Machine has 4th axis', default=0)


   .. py:attribute:: axis5
      :type:  BoolProperty(name='#5th Axis', description='Machine has 5th axis', default=0)


   .. py:attribute:: eval_splitting
      :type:  BoolProperty(name='Split Files', description='Split gcode file with large number of operations', default=True)


   .. py:attribute:: split_limit
      :type:  IntProperty(name='Operations per File', description='Split files with larger number of operations than this', min=1000, max=20000000, default=800000)


   .. py:attribute:: collet_size
      :type:  FloatProperty(name='#Collet Size', description='Collet size for collision detection', default=33, min=1e-05, max=320000, precision=constants.PRECISION, unit='LENGTH')


   .. py:attribute:: output_block_numbers
      :type:  BoolProperty(name='Output Block Numbers', description='Output block numbers ie N10 at start of line', default=False)


   .. py:attribute:: start_block_number
      :type:  IntProperty(name='Start Block Number', description='The starting block number ie 10', default=10)


   .. py:attribute:: block_number_increment
      :type:  IntProperty(name='Block Number Increment', description='How much the block number should increment for the next line', default=10)


   .. py:attribute:: output_tool_definitions
      :type:  BoolProperty(name='Output Tool Definitions', description='Output tool definitions', default=True)


   .. py:attribute:: output_tool_change
      :type:  BoolProperty(name='Output Tool Change Commands', description='Output tool change commands ie: Tn M06', default=True)


   .. py:attribute:: output_g43_on_tool_change
      :type:  BoolProperty(name='Output G43 on Tool Change', description='Output G43 on tool change line', default=False)


