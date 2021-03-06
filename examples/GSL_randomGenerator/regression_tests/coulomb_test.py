#!/usr/bin/python
"""
Test simple tof simulations
"""
from nose.tools import assert_equal, assert_true, assert_false
import os
from test_functions import *


class TestRegenerate(object):
    
    
    def setup(self):
        self.run_output = "testing.tmp"
        self.ref_output = "coulomb_test/output.out"
        self.description = 'coulomb_test:  '


    def teardown(self):
        os.remove('testing.tmp')
    

    def test_run(self):
        command = 'tftOccupation coulomb_test/coulomb_test.sim \
                 coulomb_test/scl_plane.edge coulomb_test/scl_plane.xyz'
        assert(run_and_check_sim(command, self.run_output))
        

    def test_mob_dis(self):
        self.test_run()
        assert equal_output(self.ref_output, self.run_output, '--mob_dis')
        

    def test_mob_vel(self):
        self.test_run()
        assert equal_output(self.ref_output, self.run_output, '--mob_vel')
    
    def test_photocurrent(self):
        self.test_run()
        assert equal_output(self.ref_output, self.run_output, '--transient')


    def test_occupation(self):
        self.test_run()
        assert equal_output(self.ref_output, self.run_output, '--occ_prob')


    def test_fail_extracting_data(self):
        self.test_run()
        assert_false(equal_output(self.ref_output, self.run_output,
                                  '--energies'))


    
