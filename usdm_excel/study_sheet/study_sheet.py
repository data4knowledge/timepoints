from usdm_excel.base_sheet import BaseSheet
from usdm_excel.study_identifiers_sheet.study_identifiers_sheet import StudyIdentifiersSheet
from usdm_excel.study_design_sheet.study_design_sheet import StudyDesignSheet
from usdm_excel.study_soa_sheet.study_soa_sheet import StudySoASheet
from model.study import Study
import traceback
import pandas as pd

class StudySheet(BaseSheet):

  def __init__(self, file_path, id_manager):
    try:
      super().__init__(pd.read_excel(open(file_path, 'rb'), sheet_name='study'), id_manager)
      self.study = None
      self.study_identifiers = StudyIdentifiersSheet(file_path, id_manager)
      self.study_design = StudyDesignSheet(file_path, id_manager)
      #self.soa = StudySoASheet(file_path, id_manager)

      #self.study_design.link_timelines(self.soa.timelines)

      #self.activities = StudyActivitiesSheet(file_path)
      #self.soa.link_study_data(self.activities.activity_map)
      #self.study_designs.link_encounters(self.soa.epoch_encounter_map)
      #self.study_designs.link_wfi(self.soa.workflow_items)
      
      print("Study 1")
      self.process_sheet()
      print("Study 2")
    except Exception as e:
      print("Oops!", e, "occurred.")
      traceback.print_exc()

  def process_sheet(self):
    for index, row in self.sheet.iterrows():
      study_phase = self.cdisc_code_cell(self.clean_cell(row, index, "studyPhase"))
      study_version = self.clean_cell(row, index, "studyVersion")
      study_type = self.cdisc_code_cell(self.clean_cell(row, index, "studyType"))
      study_title = self.clean_cell(row, index, "studyTitle")
      self.study = Study(
        studyId=None, # No Id, will be allocated a UUID
        studyTitle=study_title,
        studyVersion=study_version,
        type=study_type,
        phase=study_phase,
        ta=None,
        studyRationale="",
        studyAcronym="",
        identifiers=self.study_identifiers.identifiers,
        protocols=[],
        designs=self.study_design.study_designs
      )

  def study_sponsor(self):
    return self.cdisc_code(code="C93453", decode="Study Registry")

  def study_regulatory(self):
    return self.cdisc_code(code="C93453", decode="Study Registry")

  def the_study(self):
    return self.study