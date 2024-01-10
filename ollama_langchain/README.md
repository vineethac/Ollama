## Overview
In this exercise we will use langchain to connect and interact with Ollama/ LLM models.

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

## Prompting Ollama
Note: In your case, you may need to modify `base_url` in the python script based on where Ollama is running.

```
root@debug:/# python3 ollama-prompt.py --help
usage: ollama-prompt.py [-h] [--model MODEL]

options:
  -h, --help     show this help message and exit
  --model MODEL
root@debug:/#
root@debug:/# python3 ollama-prompt.py --model llama2
Model: llama2
Ask me anything: who are you?

I am LLaMA, an AI assistant developed by Meta AI that can understand and respond to human input in a conversational manner. I am trained on a massive dataset of text from the internet and can generate human-like responses to a wide range of topics and questions. I can be used to create chatbots, virtual assistants, and other applications that require natural language understanding and generation capabilities.


Model: llama2
Ask me anything: /bye
root@debug:/#
root@debug:/#
root@debug:/# python3 ollama-prompt.py --model mistral
Model: mistral
Ask me anything: who are you?
 I am an artificial intelligence designed to assist and communicate with people. I don't have the ability to have a personal identity or emotions. I'm here to help answer questions, provide information, and engage in conversational exchanges with you. How can I assist you today?


Model: mistral
Ask me anything: how to reverse a string in python?
 To reverse a string in Python, you can use slicing. Here's an example of how to do it:

python

# Original string
my_string = "Hello World"

# Reverse string using slicing
reversed_string = my_string[::-1]

# Print the reversed string
print(reversed_string)


In the code above, we used the slice notation `my_string[::-1]`. The `:` means "all elements," and the `-1` indicates that we want to step backwards. So, this expression returns a new string with the characters of the original string in reverse order.


Model: mistral
Ask me anything: write a python program to find the second smallest number in a given list.
 Here is a simple Python program that finds the second smallest number in a given list:

python

def find_second_smallest(numbers):
    # Check if the list has less than 2 elements
    if len(numbers) < 2:
        raise ValueError("The list should have atleast 2 elements")

    smallest = min(numbers)
    second_smallest = float('inf')

    for num in numbers:
        # If the current number is smaller than the smallest, update smallest and reset second smallest
        if num < smallest:
            second_smallest = smallest
            smallest = num
        # If the current number is not smaller than smallest but smaller than second smallest, update second smallest
        elif num != smallest and num < second_smallest:
            second_smallest = num

    return second_smallest

if __name__ == "__main__":
    numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
    print(f"The second smallest number is: {find_second_smallest(numbers)}")


This program defines a function `find_second_smallest()` that takes a list of numbers as an argument. It checks if the list has at least 2 elements, and then uses a `for` loop to iterate through all the numbers in the list. In each iteration, it updates the smallest and second smallest variables accordingly based on the current number being smaller than or equal to smallest or not. Finally, it returns the second smallest variable.


Model: mistral
Ask me anything:
```