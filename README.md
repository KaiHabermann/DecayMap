## Wanted Functionality
- List of all Particles -> Download PDGIdentifiers table form PDG website
- Properties of Particles -> Mass, Width, decay channels etc... should be loaded from PDG
    - Option 1: Get access to PDG database creating the Website entries
    - Option 2: Use Programm to grab values from PDGlive based on List of all Particles
- use potent enough database (MongoDB) to create database of particles with links for decays etc
- create query language to acces such a database


## Example Query

``SELECT p FROM DECAY(L_b) WHERE BR(L_b,p) > 1e-3``

``SELECT p from PARTICLES WHERE IS_DECAYPRODUCT(p,L_b,3,False) AND LIFETIME(p) > 1e-19``

