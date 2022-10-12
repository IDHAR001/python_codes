from skill_system.skill_deployer import *

SkillDeployer.SkillDeployer_print_age()

idhar = SkillDeployer("idhar")
idhar.SkillDeployer_print_name(idhar.name)
SkillDeployer.SkillDeployer_print_age_static()
idhar.SkillDeployer_print_age_static()

# 导包路径
import sys
sys.path.append("/Users/zzhang221/Desktop/python/code/python_codes/Fourth/Packge_demo")
print(sys.path)