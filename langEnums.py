from enum import Enum

class Exceptions(Enum):
	InvalidSyntax	= 100 # IS
	AlreadyDefined	= 101 # AD
	NotImplementedException	= 102 # NIE
	NotDefinedException		= 103 # NDE
	GeneralException		= 104 # GE
	DivideByZeroException	= 105 # DBZ
	InvalidValue			= 106 # IV
	InvalidTypeException	= 107 # ITE

class Types(Enum):
	Boolean = 0
	Integer = 1
	Float	= 2
	List	= 3
	Dictionary = 4
	Tuple	= 5
	Dynamic	= 6
	String	= 7
	Any		= 8

class ConditionType(Enum):
	And	= 0
	Or	= 1
	Single	= 2