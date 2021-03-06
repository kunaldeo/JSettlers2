/**
 * Java Settlers - An online multiplayer version of the game Settlers of Catan
 * This file Copyright (C) 2019-2020 Jeremy D Monin <jeremy@nand.net>
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 3
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * The maintainer of this program can be reached at jsettlers@nand.net
 **/

package soctest.game;

import java.util.Arrays;

import soc.game.SOCBoardLarge;

import org.junit.Test;
import static org.junit.Assert.*;

/**
 * A few tests for {@link SOCBoardLarge}.
 *
 * @see TestBoard
 * @since 2.0.00
 */
public class TestBoardLarge
{
    /**
     * For a pair of edge coordinates, test
     * {@link SOCBoardLarge#getNodeBetweenAdjacentEdges(int, int)} with parameters in both orders,
     * and {@link SOCBoardLarge#getAdjacentNodesToEdge_arr(int)}, to see if they return {@code nodeBetween}.
     * @param expectFail  True if {@code nodeBetween} isn't between the two edges
     *     and {@code getNodeBetweenAdjacentEdges} should throw {@link IllegalArgumentException}
     * @see TestBoard#doTestPair_getNodeBetweenAdjacentEdges(soc.game.SOCBoard, int, int, int, boolean)
     */
    private static void doTestPair_getNodeBetweenAdjacentEdges
        (final SOCBoardLarge board, final int edgeA, final int edgeB, final int nodeBetween, final boolean expectFail)
    {
        String desc = "getNodeBetweenAdjacentEdges(0x" + Integer.toHexString(edgeA)
            + ", 0x" + Integer.toHexString(edgeB) + ")";
        try
        {
            final int n = board.getNodeBetweenAdjacentEdges(edgeA, edgeB);
            if (expectFail)
                fail(desc + " should have thrown exception");
            assertEquals(desc + " incorrect", nodeBetween, n);
        }
        catch (IllegalArgumentException e) {
            if (! expectFail)
                throw e;
        }

        desc = "getNodeBetweenAdjacentEdges(0x" + Integer.toHexString(edgeB)
            + ", 0x" + Integer.toHexString(edgeA) + ")";
        try
        {
            final int n = board.getNodeBetweenAdjacentEdges(edgeB, edgeA);
            if (expectFail)
                fail(desc + " should have thrown exception");
            assertEquals(desc + " incorrect", nodeBetween, n);
        }
        catch (IllegalArgumentException e) {
            if (! expectFail)
                throw e;
        }

        if (expectFail)
            return;

        int[] nodes = board.getAdjacentNodesToEdge_arr(edgeA);
        assertTrue("Expected 0x" + Integer.toHexString(nodeBetween) + " in getAdjacentNodesToEdge_arr(0x"
            + Integer.toHexString(edgeA) + "), was " + Arrays.toString(nodes),
            (nodes[0] == nodeBetween) || (nodes[1] == nodeBetween));

        nodes = board.getAdjacentNodesToEdge_arr(edgeB);
        assertTrue("Expected 0x" + Integer.toHexString(nodeBetween) + " in getAdjacentNodesToEdge_arr(0x"
            + Integer.toHexString(edgeB) + "), was " + Arrays.toString(nodes),
            (nodes[0] == nodeBetween) || (nodes[1] == nodeBetween));
    }

    @Test
    public void test_getNodeBetweenAdjacentEdges()
    {
        SOCBoardLarge b = new SOCBoardLarge(null, 4, SOCBoardLarge.getBoardSize(null));

        // adjacent to vertical "|" edge
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x505, 0x404, 0x405, false);
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x505, 0x405, 0x405, false);
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x505, 0x604, 0x605, false);
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x505, 0x605, 0x605, false);
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x505, 0x505, 0, true);  // not adjacent: same edge twice
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x505, 0x503, 0, true);  // same row 1 hex away
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x505, 0x507, 0, true);  // same row
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x505, 0x403, 0, true);  // 2 edges away

        // adjacent to northeast-diagonal "/" edge
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x407, 0x406, 0x407, false);
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x407, 0x507, 0x407, false);
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x407, 0x308, 0x408, false);
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x407, 0x408, 0x408, false);
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x407, 0x407, 0, true);  // not adjacent: same edge twice
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x407, 0x206, 0, true);  // same axis 1 hex away
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x407, 0x608, 0, true);  // same axis
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x407, 0x405, 0, true);  // 2 edges away

        // adjacent to southeast-diagonal "\" edge
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x406, 0x306, 0x406, false);
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x406, 0x405, 0x406, false);
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x406, 0x407, 0x407, false);
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x406, 0x507, 0x407, false);
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x406, 0x406, 0, true);  // not adjacent: same edge twice
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x406, 0x207, 0, true);  // same axis 1 hex away
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x406, 0x605, 0, true);  // same axis
        doTestPair_getNodeBetweenAdjacentEdges(b, 0x406, 0x505, 0, true);  // 2 edges away
    }

}
