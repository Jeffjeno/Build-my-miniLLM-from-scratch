# the structure
1.easy.json
2.medium.json
3.hard.json

Thanks for the  [Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation](https://openreview.net/pdf?id=C25SgeXWjE)


  GitHub: https://github.com/opendatalab/ProverGen
  
  ## example
  ```
    {
    "id": 0,
    "options": [
      "A) True",
      "B) False",
      "C) Uncertain"
    ],
    "answer": "B",
    "question": "Based on the above information, is the following statement true, false, or uncertain? Brecken has never experienced heartbreak.",
    "reasoning": "fact1: Brecken has experienced heartbreak.\nrule: Either Brecken has experienced heartbreak or he has never experienced heartbreak, but not both.\nconclusion: Brecken has experienced heartbreak.\n\nTherefore, it is false that Brecken has never experienced heartbreak. The correct option is: B.",
    "context": "Brecken has experienced heartbreak. Either Brecken has experienced heartbreak or he has never experienced heartbreak, but not both.",
    "nl2fol": {
      "Brecken has experienced heartbreak.": "has_experienced_heartbreak(Brecken)",
      "Either Brecken has experienced heartbreak or he has never experienced heartbreak, but not both.": "has_experienced_heartbreak(Brecken) ⊕ has_never_experienced_heartbreak(Brecken)"
    },
    "conclusion_fol": "has_never_experienced_heartbreak(Brecken)"
    }
```