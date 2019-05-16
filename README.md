每段视频大概包含 10(每个摄像头下视频段数) * 10.5 （每段视频分钟数） * 60 （60秒）* 50（每秒50帧）帧，全部解帧大约占空间224GB, 时间为773分钟。每隔数帧采样的话，时间空间都可以相应倍减，DukeMTMC-VID采用的就是每隔5帧采一帧。
原材料中有9个摄像头采集的数据，Duke-VID取了其中前8个摄像头采集的数据，共有8可使用视频，相应的时空消耗 * 8。
解帧可以使用video_segment.py脚本。

然后就是Duke-VID中每段行人视频中在原始视频中的位置信息，存于CSV中。["person_id", "camera_id", "frame_id_in_origin_video", "frame_img_name", "x", "y", "w", "h"] 几个属性分别代表行人ID，摄像头ID，采集的这张行人帧在原视频中的帧的id，当前行人帧在duke-vid中的图片名称，剩下的是此行人在原视频帧中的位置信息，武宇博士的原材料是一个mat，我给转换成了csv，convert_mat_to_csv.py脚本负责了这部分工作。mat和csv存于
链接：https://pan.baidu.com/s/13UYdTYEn5b0nk7sks6J20w 
提取码：x6rq 
百度云中。
