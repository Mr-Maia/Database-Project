-- Criação da Stored Procedure para a Restrição RI-1
CREATE OR REPLACE FUNCTION age_check() RETURN TRIGGER AS $$
    BEGIN
        IF (CURRENT_DATE - INTERVAL '18 YEARS' < bdate) THEN
            RAISE EXCEPTION 'Although we agree, you cano´t explore children'
        END IF
        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;


-- Criação do Trigger para executar a Stored Procedure
CREATE TRIGGER age_check
BEFORE INSERT OR UPDATE ON employee
FOR EACH ROW --?
EXECUTE FUNCTION check_employee_age();
