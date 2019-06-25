import unittest
from exoviewer_api.python.ExpMgrApi15 import app, db
import HtmlTestRunner
import json
import requests
from locust import HttpLocust, TaskSet , task


class TestExpMgrApi15(unittest.TestCase):
    def setUp(self):
        self.ExpMgrApi15 = app.test_client()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False

    def tearDown(self):
        pass

    def test_A_startFunc(self):
        response = self.ExpMgrApi15.get('/ExperimentManager/api', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_B_getExperiments(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/getAllExperiments"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/getAllExperiments', follow_redirects=True)
        data_b = json.loads(response.data)
        # self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_C_getAnalysedExperiments(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/getAnalysedExperiments"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/getAnalysedExperiments')
        data_b = json.loads(response.data)
        # self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_D_getExperiment(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/getExpt?exptname=lvdm"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/getExpt?exptname=lvdm', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_E_createExperiment(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/createExperiment/?status=prescan"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/createExperiment/?status=prescan',
                                        follow_redirects=True)
        data_b = json.loads(response.data)
        print(data_b)
        print(data_a)
        #self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200, "Error this")
        #self.assertEqual(data_a, data_b)

    def test_F_get_plates(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/getPlates?exptid=650"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/getPlates?exptid=650', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_G_importchipsfromfile(self):
        files = {'file1': open('18K1D01.CHIP01974.xml', 'rb'), 'file2': open('18K1D01.CHIP01975.xml', 'rb'),
                 'file3': open('18K1D01.CHIP01976.xml', 'rb')}
        response = self.ExpMgrApi15.post('/ExperimentManager/api/v1.0/importchipsfromfile', data=files)
        self.assertEqual(response.status_code, 200)

    def test_H_setchipdata(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/setchipdata?sname=grade&chipid=28&time=16&type=Cyst fl" \
              "uid&dil=3&exptid=650"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/setchipdata?sname=grade&chipid=28&time=16&'
                                        'type=Cyst fluid&dil=3&exptid=650', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_I_getexptdata(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/getexptdata?exptid=650"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/getexptdata?exptid=650', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

        # changes are made to the Experiment model for this test
    def test_J_getexptchips(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/getexptchips?exptid=650"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/getexptchips?exptid=650',
                                        follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_K_getechips(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/getechips?exptid=650"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/getechips?exptid=650', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_L_updatechipdata(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/updatechipdata?echipid=709&" \
              "sname=grade&dil=3&type=Cyst fluid&time=16"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/updatechipdata?echipid=709&sname=grade&dil=3&'
                                        'type=Cyst fluid&time=16', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_M_addechip(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/addechip?exptid=650&chipid=3"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/addechip?exptid=650&chipid=3' , follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(data_a, data_b)

    def test_N_getPrescanChips(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/getPrescanChips?exptid=650"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/getPrescanChips?exptid=650')
        data_b = json.loads(response.data)
        # self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_O_remechip(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/remechip?exptid=650&chipid=3"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/remechip?exptid=650&chipid=3')
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(data_a, data_b)

    def test_P_removeExperiment(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/removeExperiment?exptid=654"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/removeExperiment?exptid=654', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_Q_fetchcombchips(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/fetchcombchips?exptid=650"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/fetchcombchips?exptid=650', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_R_setallchipdata(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/setallchipdata?exptid=650"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/setallchipdata?exptid=650', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_S_experimentById(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/getExperimentById?exptid=934"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/getExperimentById?exptid=934',
                                        follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_T_getPlatesById(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/getPlatesById?plate_id=1"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/getPlatesById?plate_id=1', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    # changes are made to the API for this test
    def test_U_getedata(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/getedata?exptid=650"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/getedata?exptid=650', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_V_ExoScanStartChip(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/startscan?exptid=650&chipid=25&scan_number=2"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/startscan?exptid=650&chipid=25&scan_number=2', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_W_exoscanspot(self):
        response = self.ExpMgrApi15.post('/ExperimentManager/api/v1.0/exoscanspot', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_X_endscan(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/endscan?exptid=650&chipid=25&scan_number=2"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/endscan?exptid=650&chipid=25&scan_number=2', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_Y_queuelength(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/queuelength"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/queuelength', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZA_temporaryInsert(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/overideInsertToQueue"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/overideInsertToQueue', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZB_getDbStatus(self):
        expected_message = "Database isn't connected"
        try:
            url = "http://localhost:5020/ExperimentManager/api/v1.0/dbstatus"
            resp = requests.get(url=url)
            data_a = resp.json()
            response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/dbstatus', follow_redirects=True)
            data_b = json.loads(response.data)
            self.assertEqual(data_a.keys(), data_b.keys())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data_a, data_b)
        except AssertionError as e:
            print(self.assertTrue(expected_message in str(e)))

    def test_ZC_ApiStatus(self):
        expected_message = "API isn't running"
        try:
            url = "http://localhost:5020/ExperimentManager/api/v1.0/apistatus"
            resp = requests.get(url=url)
            data_a = resp.json()
            response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/apistatus', follow_redirects=True)
            data_b = json.loads(response.data)
            self.assertEqual(data_a.keys(), data_b.keys())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data_a, data_b)
        except AssertionError as e:
            print((self.assertTrue(expected_message in str(e))))

    # Changes are made to the API for this test
    def test_ZD_getConfig(self):
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/getConfig?type=stack', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # changes are made to the API for this test
    def test_ZE_getChipByName(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/getChipByName?chip_id=18"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/getChipByName?chip_id=18', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    # Database issues
    def test_ZF_getunprocessedscan(self):
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/getunprocessedscan', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # changes are made to the API for this test
    def test_ZG_launchExoScan(self):
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/launchExoScan', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_ZH_retireExoScan(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/retireExoScan?process_id=14484"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/retireExoScan?process_id=14484', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZI_getPlates(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/getAllPlates"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/getAllPlates', follow_redirects=True)
        data_b = json.loads(response.data)
        # self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZJ_getPlatesById(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/getPlatesById?plate_id=1"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/getPlatesById?plate_id=1', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZK_getePlates(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/getePlates?exptid=650"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/getePlates?exptid=650', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZL_getePlatesById(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/getePlatesById?exptid=934&plate_id=2"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/getePlatesById?exptid=934&plate_id=2',
                                        follow_redirects=True)
        data_b = json.loads(response.data)
        # self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZM_displayechips(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/displayechips?exptid=650"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/displayechips?exptid=650', follow_redirects=True)
        data_b = json.loads(response.data)
        # self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZN_analyzedsummary(self):
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/experimentsummary?exptid=977', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_ZO_savesample(self):
        response = self.ExpMgrApi15.post('/ExperimentManager/api/v1.0/savesample?echipid=702&sample_name=chapter&'
                                         'dilution=3&incubation_time=16&sample_type=Cyst fluid&notes=null',
                                         follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_ZP_updateSampleName(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/updateSampleNameById?sample_id=583&sample_name=chapter"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/updateSampleNameById?sample_id=583&'
                                        'sample_name=chapter',follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZQ_updateIncubationTime(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/updateIncubationTimeBySampleId?sample_id=583&incubation" \
              "_time=16"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/updateIncubationTimeBySampleId?sample_id=583&'
                                        'incubation_time=16',follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZR_updateDilution(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/updateDilutionBySampleId?sample_id=583&dilution=3"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/updateDilutionBySampleId?sample_id=583&dilution=3',
                                        follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZS_updateSampleType(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/updateSampleTypeBySampleId?sample_id=583&type=Cystfluid"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/updateSampleTypeBySampleId?sample_id=583&'
                                        'type=Cyst fluid',follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZT_reporting(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/reporting?exptid=934"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/reporting?exptid=934', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZU_getchannels(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/getchannels"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/getchannels', follow_redirects=True)
        data_b = json.loads(response.data)
        # self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZV_change_label(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/changechlabel?channel_id=11&ch_name=CD9-488"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/changechlabel?channel_id=11&ch_name=CD9-488', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZW_addchannel(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/addchannel?channel_id=11&echip_id=CD9-488&channel_nam" \
              "e=CD9-488"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/addchannel?channel_id=11&echip_id=CD9-488&'
                                        'channel_name=CD9-488', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZX_remchannel(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/remchannel"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/remchannel', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZY_modifyExperimentName(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/modifyExperimentName?exptid=664&newName=experiment1"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/modifyExperimentName?exptid=664&'
                                        'newName=experiment1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZZA_getExperimentNotes(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/getExperimentNotes?exptid=977"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/getExperimentNotes?exptid=977', follow_redirects=True)
        data_b = json.loads(response.data)
        # self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZZB_saveExperimentNotes(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/saveExperimentNotes?exptid=650&title=Me&detai" \
              "ls=Add+chips"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/saveExperimentNotes?exptid=650&'
                                        'title=Me&details=Add+chips', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZZC_editExperimentNotesDetails(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/editExperimentNoteDetails?exptid=997&notesid=34&det" \
              "ails=979"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/editExperimentNoteDetails?exptid=997&'
                                        'notesid=34&details=979', follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZZD_editExperimentNotesBrief(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/editExperimentNotesBrief?exptid=997&notes" \
              "id=34&brief=789"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get(
            '/ExperimentManager/api/v1.0/editExperimentNotesBrief?exptid=997&notesid=34&brief=789',
            follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZZE_deleteExperimentNotes(self):
        url = "http://localhost:5020/ExperimentManager/api/v1.0/deleteExperimentNotes?exptid=997&notesid=34"
        resp = requests.get(url=url)
        data_a = resp.json()
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/deleteExperimentNotes?exptid=997&notesid=34',
                                        follow_redirects=True)
        data_b = json.loads(response.data)
        self.assertEqual(data_a.keys(), data_b.keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_a, data_b)

    def test_ZZF_get_resc(self):
        response = self.ExpMgrApi15.get('/ExperimentManager/api/v1.0/uploadform', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


class MyLocust(HttpLocust):
    task_set = TestExpMgrApi15
    min_wait = 1000
    max_wait = 2000


suite = unittest.TestLoader().loadTestsFromTestCase(TestExpMgrApi15)
unittest.TextTestRunner(verbosity=2)
output = open("results.html","w")
runner = HtmlTestRunner.HTMLTestRunner(stream=output)
runner.run(suite)


if __name__ == '__main__':
    unittest.main()





