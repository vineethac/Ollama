## Overview
In this exercise we will interact with LLaVA which is an end-to-end trained large multimodal model and vision assistant. We make use of the Ollama REST API to prompt the model using Python. 

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

{
    "model": "llava",
    "created_at": "2024-01-23T17:41:27.771729767Z",
    "response": " The image shows a man riding his bicycle on a country road, surrounded by beautiful scenery and mountains. He appears to be enjoying the ride as he navigates through the countryside. \n\nWhile cycling in such environments, an essential item one would need to carry is a water bottle or hydration pack, to ensure they stay well-hydrated during the journey. In addition, it's important to have a map or GPS device to navigate through potentially less familiar routes and avoid getting lost. Other useful items for cyclists may include a multi-tool, first aid kit, bike lock, snacks, spare clothes, and a small portable camping stove if planning an overnight stay in the wilderness.",
    "done": true,
    "context": [
        29871,
        13,
        11889,
        29901,
        8453,
        278,
        7623,
        322,
        825,
        526,
        278,
        3686,
        9409,
        393,
        697,
        817,
        304,
        8677,
        6892,
        1550,
        2675,
        1438,
        2924,
        310,
        7600,
        29973,
        13,
        22933,
        5425,
        1254,
        13566,
        29901,
        29871,
        450,
        1967,
        3697,
        263,
        767,
        364,
        4821,
        670,
        289,
        4245,
        2841,
        373,
        263,
        4234,
        6520,
        29892,
        22047,
        491,
        9560,
        5763,
        708,
        322,
        19223,
        29889,
        940,
        5692,
        304,
        367,
        11418,
        5414,
        278,
        22203,
        408,
        540,
        12402,
        1078,
        1549,
        278,
        2613,
        509,
        952,
        680,
        29889,
        29871,
        13,
        13,
        8809,
        488,
        5094,
        19914,
        297,
        1316,
        23136,
        29892,
        385,
        18853,
        2944,
        697,
        723,
        817,
        304,
        8677,
        338,
        263,
        4094,
        18046,
        280,
        470,
        27246,
        29878,
        362,
        4870,
        29892,
        304,
        9801,
        896,
        7952,
        1532,
        29899,
        29882,
        2941,
        29878,
        630,
        2645,
        278,
        16342,
        29889,
        512,
        6124,
        29892,
        372,
        29915,
        29879,
        4100,
        304,
        505,
        263,
        2910,
        470,
        402,
        7024,
        4742,
        304,
        23624,
        1549,
        19998,
        3109,
        9985,
        12049,
        322,
        4772,
        2805,
        5714,
        29889,
        5901,
        5407,
        4452,
        363,
        24502,
        2879,
        1122,
        3160,
        263,
        2473,
        29899,
        10154,
        29892,
        937,
        16226,
        413,
        277,
        29892,
        4768,
        446,
        7714,
        29892,
        5807,
        26514,
        29892,
        29337,
        22095,
        29892,
        322,
        263,
        2319,
        2011,
        519,
        4242,
        292,
        380,
        994,
        565,
        18987,
        385,
        975,
        11147,
        7952,
        297,
        278,
        281,
        2700,
        2264,
        29889
    ],
    "total_duration": 311086688223,
    "load_duration": 2637377606,
    "prompt_eval_count": 1,
    "prompt_eval_duration": 242959234000,
    "eval_count": 163,
    "eval_duration": 65284893000
}
```

## Notes
Image credits: The sample images used here are copied from [Shutterstock](https://www.shutterstock.com).

## References
* https://github.com/jmorganca/ollama/blob/main/docs/api.md
* https://ollama.ai/library/llava
