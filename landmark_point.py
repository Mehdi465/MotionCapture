from enum import Enum

### All face indices 
# Indices for various facial regions. Those indices are accurate
LEFT_EYE_INDICES = [157,158,159]  # , 
RIGHT_EYE_INDICES = [362, 382,  263, 386, 374,373,384,  398]# 380, 374,373,384,385,387,388,385,249
MOUTH_INDICES = [78, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291]
LEFT_EYEBROW_INDICES = [70, 63, 105, 66, 107, 55, 65, 52, 53, 46]
RIGHT_EYEBROW_INDICES =  [33, 160, 158, 133, 153, 144]#[336, 296, 334, 293, 300, 276, 283, 282, 295, 285] 

FOREHEAD_INDICES = [9, 10, 338, 297, 332,67,68,69,103,104,108,109,151,299,297,338,337,333]
LEFT_CHEEK_INDICES = [187, 118, 117, 120, 47, 50, 101,111,147]
RIGHT_CHEEK_INDICES = [280, 350, 426, 429, 356, 454, 249 ,266,280, 340,345,349]
LEFT_JAW_INDICES = [234, 93, 132, 58, 172, 136, 150,34,58,93,132,138,135,136,149,150,172,215]
RIGHT_JAW_INDICES = [454, 323, 366, 401, 368, 397, 356, 401, 288, 323,364,361,367,411,435,454]
LEFT_TEMPE_INDICES = [21,162]
LEFT_PAUPIERE_INDICES = [27,28,29,30]
RIGHT_TEMPE_INDICES = [251,301,356]
RIGHT_PAUPIERE_INDICES = [260,258,257,259]
NOSE_INDICES = [1,2,3,4,5,19,49,48,59,64,166,168,174,195,197,209,248,278,419,420,439]
CHIN_INDICES = [32,140,152,148,200,211,262,395,18,424]

class LandmarkPoint(Enum):
    # Right landmarks
    temple_R_B = 0
    forehead_R_002 = 1
    forehead_R_001 = 2
    forehead_R = 3
    temple_R_T = 4
    brow_T_R = 5
    brow_T_R_001 = 6
    brow_T_R_002 = 7
    brow_T_R_003 = 8
    brow_B_R = 9
    brow_B_R_001 = 10
    brow_B_R_002 = 11
    brow_B_R_003 = 12
    lid_T_R = 13
    lid_T_R_001 = 14
    lid_T_R_002 = 15
    lid_T_R_003 = 16
    lid_B_R = 17
    lid_B_R_001 = 18
    lid_B_R_002 = 19
    lid_B_R_003 = 20
    cheek_T_R = 21
    cheek_T_R_001 = 22
    cheek_B_R = 23
    cheek_B_R_001 = 24                                                                                                                              
    nose = 25
    nose_001 = 26
    nose_002 = 27
    nose_003 = 28
    nose_004 = 29
    nose_R = 30
    nose_R_001 = 31
    jaw = 32
    jaw_R = 33 
    jaw_R_001 = 34
    lip_T = 35
    lip_T_R = 36
    lip_T_R_001 = 37
    lip_B = 38
    lip_B_R = 39
    lip_B_R_001 = 40
    chin = 41
    chin_001 = 42


    # Left landmarks
    temple_L_B = 43
    forehead_L_002 = 44
    forehead_L_001 = 45
    forehead_L = 46
    temple_L_T = 47
    brow_T_L = 48
    brow_T_L_001 = 49
    brow_T_L_002 = 50
    brow_T_L_003 = 51
    brow_B_L = 52
    brow_B_L_001 = 53
    brow_B_L_002 = 54
    brow_B_L_003 = 55
    lid_T_L = 56
    lid_T_L_001 = 57
    lid_T_L_002 = 58
    lid_T_L_003 = 59
    lid_B_L = 60
    lid_B_L_001 = 61
    lid_B_L_002 = 62
    lid_B_L_003 = 63
    cheek_T_L = 64
    cheek_T_L_001 = 65
    cheek_B_L = 66
    cheek_B_L_001 = 67
    nose_L = 68
    nose_L_001 = 69
    jaw_L = 70
    jaw_L_001 = 71
    lip_T_L = 72
    lip_T_L_001 = 73
    lip_B_L = 74
    lip_B_L_001 = 75
    chin_R = 76
    chin_L = 77
    
    # Association landmark and metaring in blender
    DICT_METARING_LANDMARK_FACE = { temple_R_B : 356,
                                forehead_R_002 : 103,
                                forehead_R_001 : 87,
                                forehead_R : 109,
                                temple_R_T : 251,
                                brow_T_R : 70,
                                brow_T_R_001 : 105,
                                brow_T_R_002 : 107,
                                brow_T_R_003 : 9,
                                brow_B_R : 30,
                                brow_B_R_001 : 29,
                                brow_B_R_002 : 28,
                                brow_B_R_003 : 168,
                                lid_T_R : 33,
                                lid_T_R_001 : 159,
                                lid_T_R_002 : 158,
                                lid_T_R_003 : 133,
                                lid_B_R : 154,
                                lid_B_R_001 : 144,
                                lid_B_R_002 : 7,
                                lid_B_R_003 : 155,
                                cheek_T_R : 50,
                                cheek_T_R_001 : 47,
                                cheek_B_R : 147,
                                cheek_B_R_001 : 111,
                                nose : 5,
                                nose_001 : 4,
                                nose_002 : 1,
                                nose_003 : 19,
                                nose_004 : 2,
                                nose_R : 48,
                                nose_R_001 : 4, 
                                jaw : 152,
                                jaw_R : 58,
                                jaw_R_001 : 149,
                                lip_T : 13,
                                lip_T_R : 80,
                                lip_T_R_001 : 185,
                                lip_B : 14,
                                lip_B_R : 88,
                                lip_B_R_001 : 185,
                                chin : 18,  # not completly sure, 18 is just under the lip
                                chin_001 : 200,
                                chin_R : 185,
                                temple_L_B : 251,
                                forehead_L_002 : 332,
                                forehead_L_001 : 297,
                                forehead_L : 338,
                                temple_L_T : 356,
                                brow_T_L : 300,
                                brow_T_L_001 : 334,
                                brow_T_L_002 : 336,
                                brow_T_L_003 : 9,
                                brow_B_L : 260,
                                brow_B_L_001 : 259,
                                brow_B_L_002 : 258, 
                                brow_B_L_003 : 193,
                                lid_T_L : 388,
                                lid_T_L_001 : 375,
                                lid_T_L_002 : 385,
                                lid_T_L_003 : 382,
                                lid_B_L : 380,
                                lid_B_L_001 : 374,
                                lid_B_L_002 : 249,
                                lid_B_L_003 : 263,
                                cheek_T_L : 280,
                                cheek_T_L_001 : 349,
                                cheek_B_L : 411,
                                cheek_B_L_001 : 345,
                                nose_L : 278,
                                nose_L_001 : 4,
                                jaw_L : 288,
                                jaw_L_001 : 395,
                                lip_T_L : 310,
                                lip_T_L_001 : 291,
                                lip_B_L : 318,
                                lip_B_L_001 : 291,
                                chin_L : 291
}
    
    def 

