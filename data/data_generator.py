import numpy as np
import pandas as pd 


    # Renvoie la Dataframe Pandas qui contient notre base de donnée générée à partir de la fonction "generer".  

def generer(nb_lignes, seed: int = 99):
    np.random.seed(seed)

    # Définition des listes reprenant les entrepots et transporteurs qui nous intéressent

    entrepots = ["Entrepot_A", "Entrepot_B", "Entrepot_C"]
    transporteurs = ["Transporteur_X", "Transporteur_Y", "Transporteur_Z"]

    # Probabilité d'être  à l'heure pour chaque transporteur
    proba_a_l_heure = {
    "Transporteur_X": 0.77,
    "Transporteur_Y": 0.92,
    "Transporteur_Z": 0.86
    }

    # Df de base

    df = pd.DataFrame({
        "livraison_id": np.arange(1, nb_lignes + 1),
        "date_commande": pd.to_datetime("2025-01-01") + pd.to_timedelta(
            np.random.randint(0, 365, size=nb_lignes), unit="D"
        ),
        "entrepot": np.random.choice(entrepots, size=nb_lignes),
        "transporteur": np.random.choice(transporteurs, size=nb_lignes),
        "distance_km": np.random.randint(50, 801, size=nb_lignes),
    })

    # Association des probabilités propres à chaque transporteur 

    df["proba_a_l_heure"] = df["transporteur"].map(proba_a_l_heure)

    # Tirage aléatoire afin de déterminer si transporteur à l'heure

    tirages = np.random.rand(nb_lignes)

    # Comparaison du tirage avec la probabilité d'être à l'heure. On pourrait imaginer que c'est une comparaison temps de livraion réalisé / maximum autorisé.

    df["a_l_heure"] = tirages < df["proba_a_l_heure"]

    # Calcul du nombre de jours nécessaires pour livrer. Hypothèse de 300 km par jour, arrondi au jour le plus proche. 

    delai_prevu_jours = (1 + (df["distance_km"] / 300)).round().astype(int)

    # Calcul de la date de livraison prévue en considérant le nombre de jours de transport nécessaires.

    df["date_livraison_prevue"] = df["date_commande"] + pd.to_timedelta(delai_prevu_jours, unit="D")


    # Retard en jours (plus réaliste selon la distance)

    # 0 si à l'heure, sinon retard max dépend de la distance.
    retard_max = np.select(
    [
        df["distance_km"] <= 200,
        (df["distance_km"] > 200) & (df["distance_km"] <= 500),
        df["distance_km"] > 500
    ],
    [
        2,  # <= 200 km : retard entre 1 et 2 max
        3,  # 200-500 km : retard entre 1 et 3 max
        4   # > 500 km : retard entre 1 et 4 max
    ],
    )
    # Retard en jours (plus réaliste selon la distance)

    # 0 si à l'heure, sinon retard max dépend de la distance.

    retard_max = np.select(
        [
            df["distance_km"] <= 200,
            (df["distance_km"] > 200) & (df["distance_km"] <= 500),
            df["distance_km"] > 500
        ],
        [
            2,  # <= 200 km : retard entre 1 et 2 max
            3,  # 200-500 km : retard entre 1 et 3 max
            4   # > 500 km : retard entre 1 et 4 max
        ],
        default=3 # Tous les cas de figures sont normalement couverts. Là pour éviter un 0 renvoyé.
    )

    # Si en retard: tirer un nombre entre 1 et retard_max (inclus)
    tirage_retard = (np.random.rand(nb_lignes) * retard_max).astype(int) + 1

    df["retard_jours_(nombre)"] = np.where(df["a_l_heure"], 0, tirage_retard)

    # Date de livraison réelle
    df["date_livraison_reelle"] = df["date_livraison_prevue"] + pd.to_timedelta(df["retard_jours_(nombre)"], unit="D")

    # Coût au km par transporteur
    cout_par_km = {
        "Transporteur_X": 1.40,
        "Transporteur_Y": 1.20,
        "Transporteur_Z": 1.05
    }

    # Associer le tarif à chaque ligne
    df["cout_km_(€)"] = df["transporteur"].map(cout_par_km)

    # Calcul du coût total de transport
    df["cout_transport_(€)"] = (df["distance_km"] * df["cout_km_(€)"]).round()


    return df

if __name__ == "__main__":
    df = generer(5000)
    df.to_csv("data/transport_data.csv", index=False)
    print("Dataset généré : data/transport_data.csv")



