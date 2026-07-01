import pytest
from pytest import approx
import water_flow as w

def test_water_column_height():
    assert w.water_column_height(0,0) == 0
    assert w.water_column_height(0,10) == approx(7.5)
    assert w.water_column_height(25,0) == 25
    assert w.water_column_height(48.3,12.8) == approx(57.9)

def test_pressure_gain_from_water_height():
    assert w.pressure_gain_from_water_height(0) == 0
    assert w.pressure_gain_from_water_height(30.2) == approx(295.628,abs=0.001)
    assert w.pressure_gain_from_water_height(50) == approx(489.450,abs=0.001)

def test_pressure_loss_from_pipe():
    assert w.pressure_loss_from_pipe(0.048692,0,0.018,1.75) == 0
    assert w.pressure_loss_from_pipe(0.048692,200,0,1.75) == 0
    assert w.pressure_loss_from_pipe(0.048692,200,0.018,0) == 0
    assert w.pressure_loss_from_pipe(0.048692,200,0.018,1.75) == approx(-113.008,abs=0.001)
    assert w.pressure_loss_from_pipe(0.048692,200,0.018,1.65) == approx(-100.462,abs=0.001)
    assert w.pressure_loss_from_pipe(0.28687,1000,0.013,1.65) == approx(-61.576,abs=0.001)
    assert w.pressure_loss_from_pipe(0.28687,1800.75,0.013,1.65) == approx(-110.884,abs=0.001)

def test_pressure_loss_from_fittings():
    assert w.pressure_loss_from_fittings(0,3) == 0
    assert w.pressure_loss_from_fittings(1.65,0) == 0
    assert w.pressure_loss_from_fittings(1.65,2) == approx(-0.109,abs=0.001)
    assert w.pressure_loss_from_fittings(1.75,2) == approx(-0.122,abs=0.001)
    assert w.pressure_loss_from_fittings(1.75,5) == approx(-0.306,abs=0.001)

def test_reynolds_number():
    assert w.reynolds_number(0.048692,0) == 0
    assert w.reynolds_number(0.048692,1.65) == approx(80069,abs=1)
    assert w.reynolds_number(0.048692,1.75) == approx(84922,abs=1)
    assert w.reynolds_number(0.28687,1.65) == approx(471729,abs=1)
    assert w.reynolds_number(0.28687,1.75) == approx(500318,abs=1)

def test_pressure_loss_from_pipe_reduction():
    assert w.pressure_loss_from_pipe_reduction(0.28687,0,1,0.048692) == 0
    assert w.pressure_loss_from_pipe_reduction(0.28687,1.65,471729,0.048692) == approx(-163.744,abs=0.001)
    assert w.pressure_loss_from_pipe_reduction(0.28687,1.75,500318,0.048692) == approx(-184.182,abs=0.001)

def test_kpa_to_psi():
    assert w.kpa_to_psi(0) == 0
    assert w.kpa_to_psi(158.7) == approx(23,abs=0.1)
    assert w.kpa_to_psi(253) == approx(36.6,abs=0.1)
    assert w.kpa_to_psi(1073) == approx(155.6,abs=0.1)


pytest.main(["-v", "--tb=line", "-rN", __file__])