from enum import Enum

### All face indices 
# Indices for various facial regions. Those indices are accurate
LEFT_EYE_INDICES = [33, 133, 160, 159, 158, 157, 173, 154, 155, 145, 153, 144, 163, 7, 246]
RIGHT_EYE_INDICES = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
MOUTH_INDICES = [78, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291]
LEFT_EYEBROW_INDICES = [70, 63, 105, 66, 107, 55, 65, 52, 53, 46]
RIGHT_EYEBROW_INDICES = [336, 296, 334, 293, 300, 276, 283, 282, 295, 285]

FOREHEAD_INDICES = [9, 10, 338, 297, 332,67,68,69,103,104,108,109,151,299,297,338,337,333]
LEFT_CHEEK_INDICES = [187, 50, 101, 118, 117, 111, 120, 47, 115, 220, 237, 239, 241, 238, 20, 50, 101,111,147]
RIGHT_CHEEK_INDICES = [280, 350, 426, 429, 356, 454, 374, 249, 187 ,266,280, 340,345,349]
LEFT_JAW_INDICES = [234, 93, 132, 58, 172, 136, 150, 176, 148, 152, 377, 378, 379,34,58,93,132,138,135,136,149,150,172,215]
RIGHT_JAW_INDICES = [454, 323, 366, 401, 368, 397, 356, 452, 401, 362, 288, 323, 329,364,361,367,411,435,451,454]
LEFT_TEMPE_INDICES = [21,162]
LEFT_PAUPIERE_INDICES = [27,28,29,30]
#RIGHT_TEMPE_INDICES = [251,301,356]
RIGHT_PAUPIERE_INDICES = [260,258,257,259]
NOSE_INDICES = [1,2,3,4,5,19,49,48,50,59,64,166,168,174,195,197,209,248,278,419,420,439]
CHIN_INDICES = [32,140,152,148,200,211,262,368,395,18,424]

""" DICT_METARING_LANDMARK_FACE = { temple_R_B : 356,
                                forehead_R_002 : ,
                                forehead_R_001 : ,
                                forehead_R : ,
                                temple_R_T : 251,
                                brow_T_R : ,
                                brow_T_R_001 : ,
                                brow_T_R_002 : ,
                                brow_T_R_003 : ,
                                brow_B_R : ,
                                brow_B_R_001 : ,
                                brow_B_R_002 : ,
                                brow_B_R_003 : ,
                                lid_T_R 
                                lid_T_R_001 : ,
                                lid_T_R_002 : ,
                                lid_T_R_003 : ,
                                lid_B_R : ,
                                lid_B_R_001 : ,
                                lid_B_R_002 : ,
                                lid_B_R_003 : ,
                                cheek_T_R : ,
                                cheek_T_R_001 : ,
                                cheek_B_R : 
                                cheek_B_R_001 : ,
                                nose : ,
                                nose_001 : ,
                                nose_002 : ,
                                nose_003 : ,
                                nose_004 : ,
                                nose_R : ,
                                nose_R_001 : , 
                                jaw : ,
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
                                brow_T_L_002 = 51
                                brow_T_L_003 = 52
                                brow_B_L = 53
                                brow_B_L_001 = 54
                                brow_B_L_002 = 55
                                brow_B_L_002 = 56
                                brow_B_L_003 = 57
                                lid_T_L = 58
                                lid_T_L_001 = 59
                                lid_T_L_002 = 60
                                lid_T_L_003 = 61
                                lid_B_L = 62
                                lid_B_L_001 = 63
                                lid_B_L_002 = 64
                                lid_B_L_003 = 65
                                cheek_T_L = 66
                                cheek_T_L_001 = 67
                                cheek_B_L = 68
                                cheek_B_L_001 = 69
                                nose_L = 70
                                nose_L_001 = 71
                                jaw_L = 72
                                jaw_L_001 = 73
                                lip_T_L = 74
                                lip_T_L_001 = 75
                                lip_B_L = 76
                                lip_B_L_001 = 77

} """


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
