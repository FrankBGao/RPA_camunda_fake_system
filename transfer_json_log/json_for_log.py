from pm4py.objects.log.importer.json import factory as json_importer
from pm4py.objects.log.exporter.xes import factory as xes_exporter
from pm4py.algo.discovery.alpha import factory as alpha_factory
from pm4py.algo.discovery.inductive import factory as inductive_factory
import pm4py.objects.log.transform as log_transform
from pm4py.visualization.petrinet import factory as pn_vis_factory


import os

rename = {
    "ActivityName": "concept:name",
    "TimeStamp": "time:timestamp",
    "Event_type": "lifecycle:transition",
    "ProcessInstanceId": "case:concept:name",
}

event_log = json_importer.import_log(os.path.join("form_json.json"), parameters={"rename_map": rename})
event_log.sort()

trace_log = log_transform.transform_event_log_to_trace_log(event_log)
trace_log.sort()
trace_log.insert_trace_index_as_event_attribute()
net, marking, final_marking = alpha_factory.apply(trace_log)

for place in marking:
    print("initial marking " + place.name)
for place in final_marking:
    print("final marking " + place.name)
gviz = pn_vis_factory.apply(net, marking, final_marking, parameters={"format": "svg"})
pn_vis_factory.view(gviz)

#xes_exporter.export_log(trace_log, "form_json.xes")


net, marking, final_marking = inductive_factory.apply(trace_log)
for place in marking:
    print("initial marking " + place.name)
for place in final_marking:
    print("final marking " + place.name)
gviz = pn_vis_factory.apply(net, marking, final_marking, parameters={"format": "svg"})
pn_vis_factory.view(gviz)