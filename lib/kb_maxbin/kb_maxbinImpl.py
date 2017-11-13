# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
import json

from kb_maxbin.Utils.MaxBinUtil import MaxBinUtil
#END_HEADER


class kb_maxbin:
    '''
    Module Name:
    kb_maxbin

    Module Description:
    A KBase module: kb_maxbin
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "1.0.3"
    GIT_URL = "https://github.com/kbaseapps/kb_maxbin.git"
    GIT_COMMIT_HASH = "a8bb5ae6ea0dc5c2b951085106aaff62d7dd59c8"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.config = config
        self.config['SDK_CALLBACK_URL'] = os.environ['SDK_CALLBACK_URL']
        self.config['KB_AUTH_TOKEN'] = os.environ['KB_AUTH_TOKEN']
        #END_CONSTRUCTOR
        pass


    def run_max_bin(self, ctx, params):
        """
        :param params: instance of type "MaxBinInputParams" (required params:
           assembly_ref: Genome assembly object reference binned_contig_name:
           BinnedContig object name and output file header workspace_name:
           the name of the workspace it gets saved to. reads_list: list of
           reads object (PairedEndLibrary/SingleEndLibrary) upon which MaxBin
           will be run optional params: thread: number of threads; default 1
           reassembly: specify this option if you want to reassemble the
           bins. note that at least one reads file needs to be designated.
           prob_threshold: minimum probability for EM algorithm; default 0.8
           markerset: choose between 107 marker genes by default or 40 marker
           genes min_contig_length: minimum contig length; default 1000
           plotmarker: specify this option if you want to plot the markers in
           each contig ref:
           http://downloads.jbei.org/data/microbial_communities/MaxBin/README.
           txt) -> structure: parameter "assembly_ref" of type "obj_ref" (An
           X/Y/Z style reference), parameter "binned_contig_name" of String,
           parameter "workspace_name" of String, parameter "reads_list" of
           list of type "obj_ref" (An X/Y/Z style reference), parameter
           "thread" of Long, parameter "reassembly" of type "boolean" (A
           boolean - 0 for false, 1 for true. @range (0, 1)), parameter
           "prob_threshold" of Double, parameter "markerset" of Long,
           parameter "min_contig_length" of Long, parameter "plotmarker" of
           type "boolean" (A boolean - 0 for false, 1 for true. @range (0, 1))
        :returns: instance of type "MaxBinResult" (result_folder: folder path
           that holds all files generated by run_max_bin report_name: report
           name generated by KBaseReport report_ref: report reference
           generated by KBaseReport) -> structure: parameter
           "result_directory" of String, parameter "binned_contig_obj_ref" of
           type "obj_ref" (An X/Y/Z style reference), parameter "report_name"
           of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN run_max_bin
        print '--->\nRunning kb_maxbin.run_max_bin\nparams:'
        print json.dumps(params, indent=1)

        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        maxbin_runner = MaxBinUtil(self.config)
        returnVal = maxbin_runner.run_maxbin(params)
        #END run_max_bin

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method run_max_bin return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
