from enum import Enum
import bpy

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

class Metaring:

    # Association landmark and metaring in blender
    DICT_METARING_LANDMARK_FACE = { LandmarkPoint.temple_R_B : 356,
                                LandmarkPoint.forehead_R_002 : 103,
                                LandmarkPoint.forehead_R_001 : 87,
                                LandmarkPoint.forehead_R : 109,
                                LandmarkPoint.temple_R_T : 251,
                                LandmarkPoint.brow_T_R : 70,
                                LandmarkPoint.brow_T_R_001 : 105,
                                LandmarkPoint.brow_T_R_002 : 107,
                                LandmarkPoint.brow_T_R_003 : 9,
                                LandmarkPoint.brow_B_R : 30,
                                LandmarkPoint.brow_B_R_001 : 29,
                                LandmarkPoint.brow_B_R_002 : 28,
                                LandmarkPoint.brow_B_R_003 : 168,
                                LandmarkPoint.lid_T_R : 33,
                                LandmarkPoint.lid_T_R_001 : 159,
                                LandmarkPoint.lid_T_R_002 : 158,
                                LandmarkPoint.lid_T_R_003 : 133,
                                LandmarkPoint.lid_B_R : 154,
                                LandmarkPoint.lid_B_R_001 : 144,
                                LandmarkPoint.lid_B_R_002 : 7,
                                LandmarkPoint.lid_B_R_003 : 155,
                                LandmarkPoint.cheek_T_R : 50,
                                LandmarkPoint.cheek_T_R_001 : 47,
                                LandmarkPoint.cheek_B_R : 147,
                                LandmarkPoint.cheek_B_R_001 : 111,
                                LandmarkPoint.nose : 5,
                                LandmarkPoint.nose_001 : 4,
                                LandmarkPoint.nose_002 : 1,
                                LandmarkPoint.nose_003 : 19,
                                LandmarkPoint.nose_004 : 2,
                                LandmarkPoint.nose_R : 48,
                                LandmarkPoint.nose_R_001 : 4,
                                LandmarkPoint.jaw : 152,
                                LandmarkPoint.jaw_R : 58,
                                LandmarkPoint.jaw_R_001 : 149,
                                LandmarkPoint.lip_T : 13,
                                LandmarkPoint.lip_T_R : 80,
                                LandmarkPoint.lip_T_R_001 : 185,
                                LandmarkPoint.lip_B : 14,
                                LandmarkPoint.lip_B_R : 88,
                                LandmarkPoint.lip_B_R_001 : 185,
                                LandmarkPoint.chin : 18,  # not completly sure, 18 is just under the lip
                                LandmarkPoint.chin_001 : 200,
                                LandmarkPoint.chin_R : 185,
                                LandmarkPoint.temple_L_B : 251,
                                LandmarkPoint.forehead_L_002 : 332,
                                LandmarkPoint.forehead_L_001 : 297,
                                LandmarkPoint.forehead_L : 338,
                                LandmarkPoint.temple_L_T : 356,
                                LandmarkPoint.brow_T_L : 300,
                                LandmarkPoint.brow_T_L_001 : 334,
                                LandmarkPoint.brow_T_L_002 : 336,
                                LandmarkPoint.brow_T_L_003 : 9,
                                LandmarkPoint.brow_B_L : 260,
                                LandmarkPoint.brow_B_L_001 : 259,
                                LandmarkPoint.brow_B_L_002 : 258,
                                LandmarkPoint.brow_B_L_003 : 193,
                                LandmarkPoint.lid_T_L : 388,
                                LandmarkPoint.lid_T_L_001 : 375,
                                LandmarkPoint.lid_T_L_002 : 385,
                                LandmarkPoint.lid_T_L_003 : 382,
                                LandmarkPoint.lid_B_L : 380,
                                LandmarkPoint.lid_B_L_001 : 374,
                                LandmarkPoint.lid_B_L_002 : 249,
                                LandmarkPoint.lid_B_L_003 : 263,
                                LandmarkPoint.cheek_T_L : 280,
                                LandmarkPoint.cheek_T_L_001 : 349,
                                LandmarkPoint.cheek_B_L : 411,
                                LandmarkPoint.cheek_B_L_001 : 345,
                                LandmarkPoint.nose_L : 278,
                                LandmarkPoint.nose_L_001 : 4,
                                LandmarkPoint.jaw_L : 288,
                                LandmarkPoint.jaw_L_001 : 395,
                                LandmarkPoint.lip_T_L : 310,
                                LandmarkPoint.lip_T_L_001 : 291,
                                LandmarkPoint.lip_B_L : 318,
                                LandmarkPoint.lip_B_L_001 : 291,
                                LandmarkPoint.chin_L : 291
}

    def check_environment():
        """takes care if the metaring is existing, correctly set up etc.."""
        pass

    def get_position(result,points:dict) -> dict:
        """extract position on the image based on a dict containing all points needed
        :param result: result of mediapipe holistic process
        :param points: dict of points to be processed
        :return points_position: position of all points in parameter"""
        res_positions = {}
        # for all selected points
        for point in points:
            # get the landmark
            landmark = result.face_landmarks.landmark[points[point]]
            x = landmark.x
            y = landmark.y
            z = landmark.z
            # add 3D coordinates for the current point
            res_positions[point]=(x, y, z)

        return res_positions

    def move_one_metaring(point:int,positions:tuple):
        """Move one metaring of the blender model
        :param point: current point (Metaring) processed
        :param positions: current position of the point"""
        bpy.ops.transform.translate(value=positions, orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
                                    orient_matrix_type='GLOBAL', mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST',
                                    use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)

    def move_metaring_(points:dict):
        """move metaring position in blender"""
        for point in points:
            move_one_metaring(point,points[point])

    def store_position():
        """Storeposition in a certain file type, to be easy read by Blender or UE5"""
        pass

    def filter():
        """Filter stored animation according multiple parameters, mostly low pass band the animation to remove all buzzling """
        pass

    def filter_in_RT():
        """Filter erratic movment of uncertatiude recorded points, but in Real Time"""
        pass



