.
├── .vscode/
│   ├── workspace env for VS code
│   └── LaTeX spellcheck override
├── Code/
│   ├── HRDiagram.py <- custom script for rapidally generating HR diagrams from POSYDON Data
│   ├── Mastergrapher.ipynb <- notebook for calling HRDiagram.py, contains the calls for all generated figs, allowing easy updating
│   └── sorting.ipynb <- sorting and saving POSYDON data sections for faster loading 
├── Model Generation/
│   └── STLs generated from q's of observed systems
├── Research Process/
│   └── reserach process essay written for the symposium at COD 
└── Paper/
    ├── figs/
    │   ├── generated figures
    │   └── reused figures
    ├── .tex -> tex file which generated the paper
    └── .pdf -> the paper itself

Paper written for my Honors Indepedent Study at the College of DuPage with Professor DalSanto. As my college did not have direct access to research oppruintonies, I chose to learn latex as I figured it would be a useful skill for years to come.

This was the first project which I used LateX for, and I could not be happier I did. While it did take ~2 weeks or so to become comfortable in it, the moment I did it become way faster then working in Google docs or the like

Notable aspects of the paper
- Auto updating graphs 
    - While working on the paper I found many times I would need to change slight notation, adding Modot for example. Reimporting the graphs was both time inducing and tedius. Because of this, setup my script to automatically export the graphs with the same filename into specific folders. This allowed the graphs to be automatically in the paper, saving large quanities of time.

