-- Criação da Stored Procedure para a Restrição RI-1
CREATE OR REPLACE FUNCTION age_check() RETURNS TRIGGER AS $$
    BEGIN
        IF (CURRENT_DATE - INTERVAL '18 YEARS' < NEW.bdate) THEN
            RAISE EXCEPTION 'EMPLOYEE MUST BE AT LEAST 18 YEARS OLD!!';
        END IF;
        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;


-- Criação do Trigger para executar a Stored Procedure
CREATE TRIGGER age_check
BEFORE INSERT OR UPDATE ON employee
FOR EACH ROW
EXECUTE FUNCTION age_check();


-- Criação do Trigger para a Restrição RI-2
CREATE OR REPLACE FUNCTION check_workplace_type() RETURNS TRIGGER AS $$
DECLARE
    office_count INTEGER;
    warehouse_count INTEGER;
BEGIN
    -- Verificar se o endereço já existe na tabela "office"
    --Percorre todas as linhas da tabela e se houver um endereço do office igual o novo endereço, incrementamos o contador e guardamos na variável
    SELECT COUNT(*) INTO office_count
    FROM office
    WHERE address = NEW.address;

    -- Verificar se o endereço já existe na tabela "warehouse"
    --Percorre todas as linhas da tabela e se houver um endereço do warehouse igual o novo endereço, incrementamos o contador e guardamos na variável
    SELECT COUNT(*) INTO warehouse_count
    FROM warehouse
    WHERE address = NEW.address;

    -- Verificar as condições da restrição
    IF (office_count > 0 AND warehouse_count > 0) THEN
        RAISE EXCEPTION 'Um Workplace não pode ser simultaneamente um Office e um Warehouse.';
    ELSIF (office_count = 0 AND warehouse_count = 0) THEN
        RAISE EXCEPTION 'Um Workplace deve ser obrigatoriamente um Office ou um Warehouse.';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Criação do Trigger para executar a função de verificação
CREATE TRIGGER enforce_workplace_type
BEFORE INSERT OR UPDATE ON workplace
FOR EACH ROW
EXECUTE FUNCTION check_workplace_type();

CREATE OR REPLACE FUNCTION check_order_contains() RETURNS TRIGGER AS $$
DECLARE
    order_count INTEGER;
BEGIN
    SELECT COUNT(*) INTO order_count
    FROM contains
    WHERE order_no = NEW.order_no;

    IF(order_count = 0)THEN
        RAISE EXCEPTION 'A ORDER TEM DE FIGURAR OBRIGATORIAMENTE EM "CONTAINS"';
    END IF;
    RETURN NEW;
END
$$ LANGUAGE plpgsql;

CREATE TRIGGER enforce_order_in_contains
BEFORE INSERT OR UPDATE ON orders
FOR EACH ROW
EXECUTE FUNCTION check_order_contains();
