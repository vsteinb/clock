package clock.gates;

import java.util.Set;

import clock.enums.NodeType;
import clock.enums.Signal;

import clock.interfaces.Gate;
import clock.interfaces.Node;

public class Eradicate extends Gate {

	public Eradicate() {
		super(NodeType.GATE__ERADICATE);
	}
	public Eradicate(Set<Node> before, Set<Node> after) {
		super(NodeType.GATE__ERADICATE, before, after);
	}

	@Override
	public Signal processSignal(Signal signal) {
		// TODO
		return signal;
	}
}
