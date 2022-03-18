#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 04:46:36 2022

@author: winter_camp
"""
import pickle


operations = [{'resolution':4,
               'install_after':'Conv0_up',
               'layers':[{'operation':'none',
                           'name':'002',
                           'clusters':[]}]
               },
              {'resolution':4,
                'install_after':'Conv1',
                'layers':[{'operation':'none',
                           'name':'002',
                           'clusters':[]}]
               },
              {'resolution':8,
                'install_after':'Conv0_up',
                'layers':[{'operation':'none',
                           'name':'002',
                           'clusters':[]}]
               },
              {'resolution':8,
                'install_after':'Conv1',
                'layers':[{'operation':'none',
                           'name':'002',
                           'clusters':[]}]
               },
              {'resolution':16,
                'install_after':'Conv0_up',
                'layers':[{'operation':'scale',
                           'name':'001',
                           'scale':-3,
                           'clusters':[0,7]},
                          {'operation':'mean_filter',
                           'name':'002',
                           'kernel_size':3,
                           'clusters':[1,5,6]}]
               },
              {'resolution':16,
                'install_after':'Conv1',
                'layers':[{'operation':'sharpen',
                          'name':'003',
                          'sharpen_factor':5,
                          'with_norm':True,
                          'clusters':[]}]
               },
              {'resolution':32,
                'install_after':'Conv0_up',
                'layers':[]
               },
              {'resolution':32,
                'install_after':'Conv1',
                'layers':[]
               },
              ]



pickle.dump( operations, open( "./operation_template.p", "wb" ) )
