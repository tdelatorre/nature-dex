-- ~ Insert fields in nature_dex_zone from net data base.

INSERT INTO nature_dex_zone (ext_ref, marine, mpoly) SELECT cuadricula, bool(marino), geom FROM malla10x10_p;
INSERT INTO nature_dex_zone (ext_ref, marine, mpoly) SELECT cuadricula, bool(marino), geom FROM malla10x10_c;
