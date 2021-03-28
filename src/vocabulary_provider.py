"""
    The hebrew word list contains 127287 non-vocalized singular hebrew words, including verbs (with inflications),
    nouns, adjectives, names (people and places).

    It was collected for this project, from referenced sources in
        https://github.com/NLPH/NLPH_Resources/
    Especially:
        - http://www.mila.cs.technion.ac.il/resources_lexicons_mila.html
        - http://www.mila.cs.technion.ac.il/resources_lexicons_verbcomplements.html
        - http://www.mila.cs.technion.ac.il/resources_lexicons_stopwords.html
        - https://github.com/NLPH/NLPH_Resources/tree/master/linguistic_resources/word_lists/hebrew_verbs_eran_tomer
        - https://github.com/NLPH/NLPH_Resources/blob/master/linguistic_resources/word_lists/top_1000_hebrew_words_twitter_2018.txt

    The licensing for them is [GPL] and [CC BY 4.0], making it free for use (with acknowledgement)
     for non-commercial purposes.
"""

from typing import Set, cast
import os
import numpy as np


def get_hebrew_vocabulary() -> Set[str]:
    return cast(
        Set[str],
        np.load(
            os.path.join(
                os.path.dirname(__file__),
                os.path.pardir,
                "res",
                "hebrew_words_extended.npy",
            ),
            allow_pickle=True,
        ).item(),
    )
