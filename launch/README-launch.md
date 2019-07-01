# agbot_0/launch/

### main.launch

This launch file is to be run on a the local pc and perform the following:

+ Launch ***mapviz*** on local pc

+ Launch ***rqt_logger_level*** on local pc (optional)

+ Launch ***rqt_console*** on local pc (optional)

+ Launch ***efk.launch*** on tx2

  + Contains robot_localization nodes and tf tranforms

+ Launch ***jrk.launch*** on tx2

  + Steering acuator

+ Launch ***teleop.launch*** on tx2

  + Nodes necessary for agbot control

+ Launch ***roboclaw.launch*** on tx2

  + Agbot drive drive control

+ Launch ***emlid_gps.launch*** on tx2

  + May requrie rtklib `str2str` to utilized INDOT RTK corrections over usb (else used local wifi network)

+ Launch ***pidget_imu.launch*** on tx2

  + Inconsitenly working
