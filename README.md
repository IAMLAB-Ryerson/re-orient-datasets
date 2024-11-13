# re-orient-datasets


## CCNA

### problem

ccna_CBH2320_100589_FLAIR_time0.nii.gz(FLAIR) from _NeuroMRI_DB/CCNA/FLAIR/NIfTI/

![](./readme_pics/ccna_incorrect_orientation.PNG)

It's clearly that A-P are flipped.


### solution

note: need docker installed.

```bash
python ccna.py
```


![](./readme_pics/ccna_good.PNG)

The orientation is correct.

