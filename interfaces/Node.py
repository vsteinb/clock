package clock.interfaces;

import java.util.Set;
import java.util.HashSet;

import clock.enums.Signal;


// interface, implemented by gate & temporal fissue
public abstract class Node {

	private Set<Node> before = new HashSet<>();
	private Set<Node> next = new HashSet<>();


	protected Node() {}

	protected Node(Set<Node> before, Set<Node> next) {
		this.before = before;
		this.next = next;
	}

	public Set<Node> getNext() {
		return this.next;
	}


	// need to override
	// returns null if the signal didn't pass trough
	public abstract Signal processSignal(Signal s);

	// need to override
	public abstract String toString();

	// destroy this node after rewiring before & after nodes to each other
	public void destroy() {
		// TODO how rewire?
	}

	// needed if neighbors are destroyed
	public void removeFromBeforeNodes(Node node) {
		// remove node (all duplicates if existing)
		while (this.before.remove(node));

		// apply in reverse, too
		node.removeFromNext(this);
	}
	public void removeFromNext(Node node) {

		// remove node (all duplicates if existing)
		while (this.next.remove(node));

		// apply in reverse, too
		node.removeFromBeforeNodes(this);
	}

	public void addToBeforeNodes(Node node) {
		if (this.before.contains(node)) return;

		this.before.add(node);
		node.addToNext(this);
	}
	public void addToNext(Node node) {
		if (this.next.contains(node)) return;

		this.next.add(node);
		node.addToBeforeNodes(this);
	}
}

// TODO: automatic management of before[] every time next[] is changed
