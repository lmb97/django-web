ALTER TABLE "rel_people_instruments"
ADD CONSTRAINT rel_people_instrumentsU UNIQUE ("person","instrument");
