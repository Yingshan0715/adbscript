from ADB.Demo import set_dglc, fuzhu_of_depth, depths_of_aipl
from ADB.Demo import diaoyong_jindian, diaoyong_tracking
from ADB import set_pause, t180, swtime, somedays
from datetime import timedelta
from ADB import shan_renqun


set_dglc(2, False, 'dp', 0, 0, 2, 2, 2, '雅培')

tAs = t180
tIs = t180
tHs = somedays('2019-3-7', 90)
tpend = '2019-3-9'


#fuzhu_of_depth(tAs, tIs, tHs, tpend, sousuoci, pph=False)
#depths_of_aipl(tAs, tIs, tpend)


t2bef = '2019-3-10'
t2end = '2019-3-13'

#diaoyong_jindian(t2bef, t2end)
#diaoyong_tracking(t2bef, t2end, tpend, 'bg')
#diaoyong_tracking(t2bef, t2end, tpend, 'scjg')
#diaoyong_tracking(t2bef, t2end, tpend, 'jg')
#diaoyong_tracking(t2bef, t2end, tpend, 'gm')
diaoyong_tracking(t2bef, t2end, tpend, 'jd')



