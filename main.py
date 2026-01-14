from pyscript import Element

def compute_average():
    
    score1 = float(Element("score1").value)
    score2 = float(Element("score2").value)

   
    average = (score1 + score2) / 2

    
    Element("average").element.innerText = f"Average: {average:.1f}"

    
    if average >= 75:
        Element("status").element.innerText = "Passed? Yes"
    else:
        Element("status").element.innerText = "Passed? No"
