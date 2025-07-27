
BASE_URL = 'https://patriotweb.gmu.edu/pls/prod/bwck'

ENDPOINTS = {
  "dyn_sched": "schd.p_disp_dyn_sched",
  "term_date": "gens.p_proc_term_date",
  "crse_unsec": "schd.p_get_crse_unsec",
  "detail_sched": "schd.p_disp_detail_sched"
}

TERM_DATE_VALUES = {
    
}

CRSE_UNSC_VALUES = {
  "term_in": "",

  "sel_subj": ["dummy", ""],
  "sel_schd": ["dummy", "%"],
  "sel_camp": ["dummy", "%"],
  "sel_levl": ["dummy", "%"],
  "sel_ptrm": ["dummy", "%"],
  "sel_instr": ["dummy", "%"],
  
  "sel_day": "dummy",
  "sel_insm": "dummy",
  "sel_sess": "dummy",
  "sel_attr": "dummy",
  
  "sel_crse": "",
  "sel_title": "",
  "sel_from_cred": "",
  "sel_to_cred": "",
  
  "begin_hh": "0",
  "begin_mi": "0",
  "begin_ap": "a",
  "end_hh": "0",
  "end_mi": "0",
  "end_ap": "a"
}
