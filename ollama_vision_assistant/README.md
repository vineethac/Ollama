## Overview
In this exercise we will interact with LLaVA which is an end-to-end trained large multimodal model and vision assistant. We make use of the Ollama REST APIs to prompt the model using Python. 

Note: In my case I am running Ollama on a Kubernetes cluster and is exposed using a service named ollama and I am connecting to it from a pod deployed inside the same K8s cluster.

```
❯ KUBECONFIG=gckubeconfig k get po -o wide
NAME                                                           READY   STATUS    RESTARTS   AGE     IP             NODE                                             NOMINATED NODE   READINESS GATES
debug                                                          1/1     Running   0          5d16h   192.168.5.9    tkc01-worker-nodepool-a1-pqq7j-fd5784bcc-9r6t5   <none>           <none>
ingress-controller-ingress-nginx-controller-5c4bb99757-z6brl   1/1     Running   0          5d20h   192.168.3.9    tkc01-worker-nodepool-a1-pqq7j-fd5784bcc-5m5v8   <none>           <none>
ollama-5f8db8bff5-gpg25                                        1/1     Running   0          5d15h   192.168.1.21   tkc01-worker-nodepool-a1-pqq7j-fd5784bcc-mszdm   <none>           <none>
❯
❯ KUBECONFIG=gckubeconfig k get svc,ep ollama
NAME             TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)     AGE
service/ollama   ClusterIP   10.102.96.6   <none>        11434/TCP   7d9h

NAME               ENDPOINTS            AGE
endpoints/ollama   192.168.1.21:11434   7d9h
❯
❯ KUBECONFIG=gckubeconfig k exec -it debug -- bash
root@debug:/#
root@debug:/# curl ollama:11434
Ollama is runningroot@debug:/#
root@debug:/#
root@debug:/#

```

## Prompting the model
Note: In your case, you may need to modify `url` in the python script based on where Ollama is running.

```
root@debug:/# python3 query_image.py --help
usage: query_image.py [-h] [--path PATH] [--prompt PROMPT]

options:
  -h, --help       show this help message and exit
  --path PATH
  --prompt PROMPT

root@debug:/# python3 query_image.py --path=images/stock-photo-biker-riding-scenic-path-in-beautiful-summer-mountain-scenery-dolomites-italy-european-alps-1802223193.jpg --prompt="describe the picture and what are the essentials that one need to carry generally while going these kind of places?"

{'model': 'llava', 'created_at': '2024-01-23T17:04:41.61517208Z', 'response': '\nThe image depicts a man riding a bicycle down a country road, surrounded by grassy fields. He is enjoying the scenic beauty of the countryside as he rides his bike. It appears to be a sunny day with good weather conditions for outdoor activities such as cycling. \n\nWhen going on similar nature trips or cycling excursions, one should generally carry essential items like water bottles, snacks, a small first aid kit, sunscreen, insect repellent, comfortable clothing, and any necessary tools to keep the bicycle in good working condition. Additionally, carrying a map or GPS device can help in case of getting lost or unfamiliar with the area.', 'done': True, 'context': [29871, 13, 11889, 29901, 8453, 278, 7623, 322, 825, 526, 278, 3686, 9409, 393, 697, 817, 304, 8677, 6892, 1550, 2675, 1438, 2924, 310, 7600, 29973, 13, 22933, 5425, 1254, 13566, 29901, 29871, 13, 1576, 1967, 1401, 919, 29879, 263, 767, 364, 4821, 263, 289, 4245, 2841, 1623, 263, 4234, 6520, 29892, 22047, 491, 17455, 29891, 4235, 29889, 940, 338, 11418, 5414, 278, 5763, 293, 15409, 310, 278, 2613, 509, 952, 680, 408, 540, 364, 2247, 670, 4768, 446, 29889, 739, 5692, 304, 367, 263, 6575, 1460, 2462, 411, 1781, 14826, 5855, 363, 714, 17433, 14188, 1316, 408, 5094, 19914, 29889, 29871, 13, 13, 10401, 2675, 373, 2788, 5469, 3367, 567, 470, 5094, 19914, 5566, 1295, 1080, 29892, 697, 881, 6892, 8677, 18853, 4452, 763, 4094, 18046, 793, 29892, 5807, 26514, 29892, 263, 2319, 937, 16226, 413, 277, 29892, 6575, 10525, 29892, 17564, 1634, 514, 296, 29892, 25561, 1067, 6046, 29892, 322, 738, 5181, 8492, 304, 3013, 278, 289, 4245, 2841, 297, 1781, 1985, 4195, 29889, 19814, 29892, 19436, 263, 2910, 470, 402, 7024, 4742, 508, 1371, 297, 1206, 310, 2805, 5714, 470, 443, 8302, 4447, 411, 278, 4038, 29889], 'total_duration': 352777387381, 'load_duration': 49089742070, 'prompt_eval_count': 1, 'prompt_eval_duration': 241327458000, 'eval_count': 157, 'eval_duration': 61840173000}
```

## Notes


## References