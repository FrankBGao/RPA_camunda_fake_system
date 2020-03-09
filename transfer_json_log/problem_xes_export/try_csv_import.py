from pm4py.objects.log.importer.csv import factory as csv_importer
import pm4py.objects.log.transform as log_transform
from pm4py.objects.log.exporter.xes import factory as xes_exporter
import os

event_log = csv_importer.import_log(os.path.join("running-example.csv"))
event_log.sort()
trace_log = log_transform.transform_event_log_to_trace_log(event_log)

trace_log.sort()
trace_log.sample()
trace_log.insert_trace_index_as_event_attribute()
xes_exporter.export_log(trace_log, "export_running-example.xes")

