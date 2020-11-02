package clock.temporalfissures;

import java.util.Set;

import clock.enums.NodeType;
import clock.enums.Signal;

import clock.interfaces.Node;
import clock.interfaces.TemporalFissure;


public class Looper extends TemporalFissure {

	public Looper() {
		super(NodeType.TEMPORAL__LOOPER);
	}
	public Looper(Set<Node> before, Set<Node> next) {
		super(NodeType.TEMPORAL__LOOPER, before, next);
	}

	@Override
	public Signal processSignal(Signal signal) {
		// TODO
		return signal;
	}
}
