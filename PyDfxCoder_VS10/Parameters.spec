[__many__]
a = float
Type = string
InputFileList = string
OutputFileList = string
OriginX = float
OriginY = float
OriginZ = float
CustomAxisXVector = float
CustomAxisYVector = float
CustomAxisZVector = float
OriginAxisX = string
OriginAxisY = string
OriginAxisZ = string
Transformation = string
Layer = string
Color = int
AxisXMapping = string

	[[Origin]]
	___many___ = float

	[[Target]]
	___many___ = list

	[[Transformation mapping]]
		[[[__many__]]]
		Mapping = str
		Scale = float
		Origin = float