INSERT INTO nature_dex_zone (ext_ref, marine, mpoly) SELECT cuadricula, bool(marino), geom FROM malla10x10_p;
INSERT INTO nature_dex_zone (ext_ref, marine, mpoly) SELECT cuadricula, bool(marino), geom FROM malla10x10_c;
