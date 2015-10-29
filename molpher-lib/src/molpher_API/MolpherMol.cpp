
#include "molpher_API/MolpherMol.hpp"

MolpherMol::MolpherMol() : mol(new MolpherMolecule()) {
    // no action
}


MolpherMol::MolpherMol(const std::string& smile) {
    std::string temp(smile);
    mol = new MolpherMolecule(temp);
}

MolpherMol::MolpherMol(MolpherMolecule& mol) {
    this->mol = &mol;
}

MolpherMolecule& MolpherMol::getMol() {
    return *mol;
}

std::string MolpherMol::getSMILES() {
    return mol->smile;
}

double MolpherMol::getDistToTarget() {
    return mol->distToTarget;
}

std::string MolpherMol::getParentSMILES() {
    return mol->parentSmile;
}

